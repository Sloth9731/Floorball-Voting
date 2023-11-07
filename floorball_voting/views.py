from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Game, Vote, Player
from django.db.models import Sum
from .forms import VoteForm
from django.shortcuts import redirect
from collections import Counter, defaultdict
from django.contrib.auth.decorators import login_required

def select_game(request):
    games = Game.objects.all()
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

def player_votes(request, player_id):

    player = get_object_or_404(Player, pk=player_id)

    game_votes = {}

    # Query all votes associated with this player
    votes_3_points = Vote.objects.filter(vote_3_points_player=player)
    votes_2_points = Vote.objects.filter(vote_2_points_player=player)
    votes_1_point = Vote.objects.filter(vote_1_point_player=player)

    # Collect all votes in a structured way
    for vote in votes_3_points:
        game_votes.setdefault(vote.game, {'3': 0, '2': 0, '1': 0})['3'] += 1
    for vote in votes_2_points:
        game_votes.setdefault(vote.game, {'3': 0, '2': 0, '1': 0})['2'] += 1
    for vote in votes_1_point:
        game_votes.setdefault(vote.game, {'3': 0, '2': 0, '1': 0})['1'] += 1

    context = {
        'player': player,
        'game_votes': game_votes,
    }
    return render(request, 'player_votes.html', context)
