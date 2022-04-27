from django.contrib import admin
from .models import Game, Winner, Kit

# Register your models here.

admin.site.register(Game)
admin.site.register(Winner)
admin.site.register(Kit)
