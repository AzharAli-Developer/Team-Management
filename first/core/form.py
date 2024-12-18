from django import forms
from .models import Player,Team,Match
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm


class LogInForm(AuthenticationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password']


class SignUpform(UserCreationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password1','password2']


class Change_Password_Form(PasswordChangeForm):
    old_password =forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 =forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 =forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']


class PlayerForm(forms.ModelForm):
    team=forms.ModelChoiceField(queryset=Player.objects.all(),label='Team',widget=forms.Select(attrs={'class':'form-control'}))
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    age=forms.CharField(label='Age',widget=forms.TextInput(attrs={'class':'form-control'}))
    height=forms.CharField(label='Height',widget=forms.TextInput(attrs={'class':'form-control'}))
    position=forms.CharField(label='Position',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=Player
        fields=['id','team','name','age','height','position']


class TeamForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    score = forms.CharField(label='Score', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=Team
        fields=['id','name','score']


class MatchForm(forms.ModelForm):
    player=forms.ModelChoiceField(queryset=Player.objects.all(),label='Player',widget=forms.Select(attrs={'class':'form-control'}))
    team_A=forms.ModelChoiceField(queryset=Team.objects.all(),label='Team A',widget=forms.Select(attrs={'class':'form-control'}))
    team_B=forms.ModelChoiceField(queryset=Team.objects.all(),label='Team B',widget=forms.Select(attrs={'class':'form-control'}))
    status=forms.CharField(label='Status',widget=forms.TextInput(attrs={'class':'form-control'}))
    minutes_played=forms.CharField(label='Minutes Played',widget=forms.TextInput(attrs={'class':'form-control'}))
    assist=forms.CharField(label='Assist',widget=forms.TextInput(attrs={'class':'form-control'}))
    rebound=forms.CharField(label='Rebound',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=Match
        fields=['id','player','team_A','team_B','status','minutes_played','assist','rebound']