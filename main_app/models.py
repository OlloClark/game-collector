from django.db import models
from django.urls import reverse

# Create your models here.

WINS = (
	("E", "easy"),
	("B", "balanced"),
	("C", "close"),
)

class Game(models.Model):
	name = models.CharField(max_length=100)
	min_players = models.PositiveIntegerField()
	max_players = models.PositiveIntegerField()
	play_time = models.PositiveIntegerField()
	played_before = models.BooleanField()
	notes = models.TextField(max_length=500)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('detail', kwargs={'game_id': self.id})

class Winner(models.Model):
	winner = models.CharField(max_length=300)
	date = models.DateField("win date")
	win = models.CharField(
		max_length=1,
		choices=WINS,
		default=WINS[0][1]
	)
	# creates a game_id FK:
	game = models.ForeignKey(Game, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.winner} won on {self.date}"

	class Meta:
		ordering = ['-date']
	
