from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import WinnerForm

# Create your views here.

class GameCreate(CreateView):
	model = Game
	fields = "__all__"

class GameUpdate(UpdateView):
  model = Game
  fields = ["min_players", "max_players", "play_time", "played_before", "notes"]

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'


# Define the home view
def home(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

def games_index(request):
	games = Game.objects.all()
	return render(request, "games/index.html", {"games": games})

def game_detail(request, game_id):
	game = Game.objects.get(id=game_id)
	kits_not_in_game = Kit.objects.exclude(id__in = game.kits.all().values_list("id"))
	winner_form =WinnerForm()
	return render(request, "games/detail.html", {
		"game": game, "winner_form": winner_form,
		"kit": kits_not_in_game
	})

def add_winner(request, game_id):
  form = WinnerForm(request.POST)
  if form.is_valid():
    new_winner = form.save(commit=False)
    new_winner.game_id = game_id
    new_winner.save()
  return redirect('detail', game_id=game_id)
	
