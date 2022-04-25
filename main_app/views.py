from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# TEMP DATA
class Game:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, publisher, players, theme):
    self.name = name
    self.publisher = publisher
    self.players = players
    self.theme = theme
	
games = [
  	Game("Snap", "card games", 2, "easy time-passing"),
  	Game("snakes n ladders", "hasbro", 2, "mindless chance"),
]

# Define the home view
def home(request):
	return HttpResponse('<h1>Game Collector Home Page</h1>')

def about(request):
	return render(request, "about.html")

def games_index(request):
	return render(request, "games/index.html", {"games": games})

	
