from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Game, Vote, Player
from django.db.models import Sum, F
from .forms import VoteForm
from django.shortcuts import redirect
from collections import Counter, defaultdict
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def select_game(request):
    games = Game.objects.all().order_by('-date')  
    return render(request, 'select_game.html', {'games': games})


def vote(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    
    if request.method == 'POST':
        form = VoteForm(request.POST)
        
        if form.is_valid():
            vote = form.save(commit=False)
            vote.game = game
    
    # Use the correct field names from your model
            vote.vote_3_points_player = form.cleaned_data['vote_3_points_player']
            vote.vote_2_points_player = form.cleaned_data['vote_2_points_player']
            vote.vote_1_point_player = form.cleaned_data['vote_1_point_player']   
            vote.save()

            return redirect('select_game')
        print("Form is not valid")
        print(form.errors)

    else:
        form = VoteForm(initial={'game': game})

    return render(request, 'vote.html', {'form': form, 'game': game})


@login_required
def player_votes(request):
    players = Player.objects.all()
    selected_player_id = request.GET.get('player_id')
    game_votes = {}
    total_votes = 0
    grand_total_votes = 0
    selected_player = None

    if selected_player_id:
        selected_player = get_object_or_404(Player, pk=selected_player_id)
        votes_3_points = Vote.objects.filter(vote_3_points_player=selected_player)
        votes_2_points = Vote.objects.filter(vote_2_points_player=selected_player)
        votes_1_point = Vote.objects.filter(vote_1_point_player=selected_player)

        # Collect all votes in a structured way
        for vote in votes_3_points:
            game_votes.setdefault(vote.game, {'3': 0, '2': 0, '1': 0})['3'] += 1
        for vote in votes_2_points:
            game_votes.setdefault(vote.game, {'3': 0, '2': 0, '1': 0})['2'] += 1
        for vote in votes_1_point:
            game_votes.setdefault(vote.game, {'3': 0, '2': 0, '1': 0})['1'] += 1

        # Calculate totals
        for votes in game_votes.values():
            total_votes += votes['3'] + votes['2'] + votes['1']
            grand_total_votes += votes['3'] * 3 + votes['2'] * 2 + votes['1'] * 1

    context = {
        'players': players,
        'selected_player': selected_player,
        'game_votes': game_votes,
        'total_votes': total_votes,
        'grand_total_votes': grand_total_votes,
    }
    return render(request, 'player_votes.html', context)


def statistics(request):
    sort_by = request.GET.get('sort', 'name')  
    if sort_by not in ['name', 'goals', 'assists', 'match_votes', 'penalties']:
        sort_by = 'name'  

    players = Player.objects.all().order_by(F(sort_by).desc(nulls_last=True))  # Sort by specified field

    context = {
        'players': players,
        'sort_by': sort_by,
    }
    return render(request, 'statistics.html', context)
