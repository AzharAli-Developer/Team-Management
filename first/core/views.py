from django.shortcuts import render,redirect
from .models import Player,Team,Match
from django.contrib import messages
from itertools import zip_longest
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login,logout,authenticate
from .form import PlayerForm,TeamForm,MatchForm,LogInForm,SignUpform,Change_Password_Form

# Create your views here.

def index(request):
    return render(request,'index.html')


def change_password(request):
    user=request.user
    if request.method== 'POST':
        form=Change_Password_Form(user=user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,user)
            return redirect('index')
    else:
        form=Change_Password_Form(user=user)
    return render(request,'change_password.html',{'form':form})


def home(request):
    match=Match.objects.all()
    return render(request,'home.html',{'match':match})


def logIn(request):
    if request.method =='POST':
        form=LogInForm(request,request.POST)
        if form.is_valid():
            un=form.cleaned_data['username']
            pw=form.cleaned_data['password']
            user=authenticate(request,username=un,password=pw)
            if user is not None:
                login(request,user)
                return redirect(request.GET.get('next', 'home'))
            else:
                messages.error(request, "Invalid username or password.")  # Error message
    form=LogInForm()
    return render(request,'logIn.html',{'form':form})


def logOut(request):
    logout(request)
    return redirect('index')


def match(request):
    if request.method == 'POST':
        form=MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=MatchForm()
    return render(request,'add_match.html',{'form':form})


def matches(request):
    return render(request,'matches.html')


def match_detail(request, id):
    match = Match.objects.get(pk=id)
    player_A = Player.objects.filter(team=match.team_A)
    player_B = Player.objects.filter(team=match.team_B)
    paired_players = zip_longest(player_A, player_B, fillvalue=None)  # Fill with `None` if lists are uneven
    context = {
        'match': match,
        'paired_players': paired_players,
    }
    return render(request, 'match_details.html', context)


def delete_match(request,id):
    match=Match.objects.get(pk=id)
    match.delete()
    return redirect('home')


def player(request):
    if request.method == 'POST':
        form=PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = PlayerForm()
    return render(request,'add_player.html',{'form':form})


def players(request):
    players=Player.objects.all()
    return render(request,'players.html',{'players':players})


def player_details(request,id):
    p=Player.objects.get(pk=id)
    match=Match.objects.get(player=p)
    context={
        'p': p,
        'match':match
    }
    return render(request,'player_details.html',context)


def signUp(request):
    if request.method == 'POST':
        form=SignUpform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logIn')
    form=SignUpform()
    return render(request,'signUp.html',{'form':form})


def team(request):
    if request.method == 'POST':
        form=TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=TeamForm()
    return render(request,'add_team.html',{'form':form})


def teams(request):
    teams=Team.objects.all()
    return render(request,'teams.html',{'teams':teams})


def team_detail(request,id):
    team=Team.objects.get(pk=id)
    players=Player.objects.filter(team=team)
    return render(request,'team_detail.html',{'players':players})