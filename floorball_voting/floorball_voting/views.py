from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Game, Vote
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
            
            # Ensure player votes are being saved
            vote.vote_3_points = form.cleaned_data['vote_3_points']
            vote.vote_2_points = form.cleaned_data['vote_2_points']
            vote.vote_1_point = form.cleaned_data['vote_1_point']

            # For debugging purposes, print out the vote details
            print("3 Points:", form.cleaned_data['vote_3_points'])
            print("2 Points:", form.cleaned_data['vote_2_points'])
            print("1 Point:", form.cleaned_data['vote_1_point'])

            vote.save()
            print("Vote Saved:", vote.id)
            return redirect('select_game')

        print("Form is not valid")
        print(form.errors)

    else:
        form = VoteForm(initial={'game': game})

    return render(request, 'vote.html', {'form': form, 'game': game})


@login_required
def display_total_points(request):
    votes = Vote.objects.all()
    all_games_points = Counter()

    for vote in votes:
        all_games_points[vote.vote_3_points] += 3
        all_games_points[vote.vote_2_points] += 2
        all_games_points[vote.vote_1_point] += 1

    sorted_all_games = sorted(all_games_points.items(), key=lambda x: x[1], reverse=True)

    context = {
        'all_games': sorted_all_games,
        'games': Game.objects.all(),
    }

    return render(request, 'total_points.html', context)

@login_required
def display_game_points(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    votes = Vote.objects.filter(game=game)

    game_points = Counter()

    for vote in votes:
        game_points[vote.vote_3_points] += 3
        game_points[vote.vote_2_points] += 2
        game_points[vote.vote_1_point] += 1

    sorted_game_points = sorted(game_points.items(), key=lambda x: x[1], reverse=True)

    context = {
        'game_points': sorted_game_points,
        'game': game,
    }

    return render(request, 'game_points.html', context)