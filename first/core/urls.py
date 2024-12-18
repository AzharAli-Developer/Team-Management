from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('change_password',views.change_password,name='change_password'),
    path('home',views.home,name='home'),
    path('loginn', views.logIn, name='loginn'),
    path('logOut', views.logOut, name='logOut'),
    path('match', views.match, name='match'),
    path('match_detail/<int:id>', views.match_detail, name='match_detail'),
    path('delete_match/<int:id>', views.delete_match, name='delete_match'),
    path('player', views.player, name='player'),
    path('players', views.players, name='players'),
    path('player_details/<int:id>', views.player_details, name='player_details'),
    path('signUp', views.signUp, name='signUp'),
    path('team', views.team, name='team'),
    path('teams', views.teams, name='teams'),
    path('team_detail/<int:id>', views.team_detail, name='team_detail'),

]