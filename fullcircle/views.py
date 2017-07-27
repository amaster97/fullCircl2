from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import SeekerSignUpForm, RecruiterSignUpForm
from users.models import User



def home(request):
    if request.user.is_authenticated():

        results = User.objects.filter(isSeeker=(not request.user.isSeeker))

        return render(request, 'dashboard.html', {'results' : results})
    else:
        return render(request, 'home.html')


def signup(request):
	return render(request, 'signup.html')

def signupSeeker(request):
    if request.method == 'POST':
        form = SeekerSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.first_name = form.cleaned_data.get('First_Name')
            user.last_name = form.cleaned_data.get('Last_Name')
            user.email = form.cleaned_data.get('Email')
            user.Birth_Date = form.cleaned_data.get('Birth_Date')

            user.Bio = form.cleaned_data.get('Bio')
            user.Profile_Picture = form.cleaned_data.get('Profile_Picture')

            user.Education_Level = form.cleaned_data.get('Education_Level')
            user.Education_Level_Priority = form.cleaned_data.get('Education_Level_Priority')
            user.Institution = form.cleaned_data.get('Institution')

            user.Sponsorship = form.cleaned_data.get('Sponsorship')
            user.Sponsorship_Priority = form.cleaned_data.get('Sponsorship_Priority')

            user.Skills = form.cleaned_data.get('Skills')
            user.Skills_Priority = form.cleaned_data.get('Skills_Priority')

            user.Industry = form.cleaned_data.get('Industry')
            user.Industry_Priority = form.cleaned_data.get('Industry_Priority')

            user.Location = form.cleaned_data.get('Location')
            user.Location_Priority = form.cleaned_data.get('Location_Priority')

            user.isSeeker = True
            
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SeekerSignUpForm()
    return render(request, 'seekersignup.html', {'form': form})

def signupRecruiter(request):
    if request.method == 'POST':
        form = RecruiterSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.first_name = form.cleaned_data.get('First_Name')
            user.last_name = form.cleaned_data.get('Last_Name')
            user.email = form.cleaned_data.get('Email')
            user.Birth_Date = form.cleaned_data.get('Birth_Date')

            user.Bio = form.cleaned_data.get('Bio')
            user.Profile_Picture = form.cleaned_data.get('Profile_Picture')

            user.Education_Level = form.cleaned_data.get('Education_Level')
            user.Education_Level_Priority = form.cleaned_data.get('Education_Level_Priority')
            user.Institution = form.cleaned_data.get('Institution')

            user.Sponsorship = form.cleaned_data.get('Sponsorship')
            user.Sponsorship_Priority = form.cleaned_data.get('Sponsorship_Priority')

            user.Skills = form.cleaned_data.get('Skills')
            user.Skills_Priority = form.cleaned_data.get('Skills_Priority')

            user.Industry = form.cleaned_data.get('Industry')
            user.Industry_Priority = form.cleaned_data.get('Industry_Priority')

            user.Location = form.cleaned_data.get('Location')
            user.Location_Priority = form.cleaned_data.get('Location_Priority')

            user.isSeeker = False
            
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RecruiterSignUpForm()
    return render(request, 'recruitersignup.html', {'form': form})

def login_views(request):
	return render(request, 'login.html')

def logout_views(request):
	logout(request)
	return home(request)

def update_profile(request):
    if request.user.is_authenticated():
        if request.user.isSeeker:
            form = SeekerSignUpForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return home(request)
        else:
            form = RecruiterSignUpForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return home(request)
        return render(request, 'update_profile.html', {'form': form})
    else:
        return render(request, 'home.html')

def matches(request):
    if request.user.is_authenticated():

        results = User.objects.filter(isSeeker=(not request.user.isSeeker))

        return render(request, 'matches.html', {'results' : results})
    else:
        return render(request, 'home.html')

def pending(request):
    if request.user.is_authenticated():
        
        return render(request, 'pending.html')
    else:
        return render(request, 'home.html')

def method(request):
	return render(request, 'method.html')