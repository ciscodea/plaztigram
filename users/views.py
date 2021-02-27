
# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm, SignupForm

@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']

            profile.save()
            return redirect('users:update_profile')
            
    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', context={'profile': profile, 'user': request.user, 'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts:feed')
    else:    
        if request.method == 'POST':
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password =password)
            if user:
                login(request, user)
                return redirect('posts:feed')
            else:
                return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

def signup(request):
    """signup view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')