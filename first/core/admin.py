from django.contrib import admin
from .models import Player,Team,Match
# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id','team','name','age','dob','height','position']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','score']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['id','player','team_A','team_B','date_of_match','status','minutes_played','assist','rebound']