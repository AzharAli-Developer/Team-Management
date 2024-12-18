from django.db import models
from datetime import datetime

class Team(models.Model):
    name=models.CharField(max_length=255)
    score=models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    dob=models.DateTimeField(auto_now_add=True)
    height=models.IntegerField()
    position=models.CharField(max_length=255)

    def __str__(self):
        return self.name


MATCH_STATUS=[
    ("Upcoming","Upcoming"),
    ("Pending","Pending"),
    ("Paused","Paused"),
    ("Completed","Completed"),
    ("Canceled","Canceled"),
    ("Postponed","Postponed"),
    ("Tie","Tie"),
]


class Match(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    team_A = models.ForeignKey('Team', related_name='home_matches', on_delete=models.CASCADE)
    team_B = models.ForeignKey('Team', related_name='away_matches', on_delete=models.CASCADE)
    date_of_match = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=MATCH_STATUS, max_length=255)
    minutes_played = models.IntegerField()
    assist = models.IntegerField()
    rebound = models.IntegerField()
