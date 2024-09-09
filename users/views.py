from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError
import re

from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

def loginPage(request):

    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get()
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, 'users/login_register.html', context)

def logoutPage(request):
    logout(request)
    messages.error(request, "User was logged out")
    return redirect('login')

# ///////////////////////// REGISTER ////////////////////////////////////////////////////////////////////////////////

# ============MAIN REGISTER FUNC=====================
def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm
    context = {'page': page, 'form': form}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('profiles')
        
        else:
            messages.success(request, 'An error was occurred during registration')

    return render(request, 'users/login_register.html', context)
# ============MAIN REGISTER FUNC=====================

# ///////////////////////// REGISTER ////////////////////////////////////////////////////////////////////////////////

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)