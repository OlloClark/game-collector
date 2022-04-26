from django.db import models

# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length=100)
	min_players = models.PositiveIntegerField()
	max_players = models.PositiveIntegerField()
	play_time = models.PositiveIntegerField()
	played_before = models.BooleanField()
	notes = models.TextField(max_length=500)

	def __str__(self):
		return self.name