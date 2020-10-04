from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('input_data')
    else:
        return render(request, 'users/login.html')

def registration_page(request):
    return render(request, 'users/registration_page.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password==password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken!')
                return redirect('registration_page')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is laready in use!')
                    return redirect('registration_page')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords donot match')
            return redirect('registration_page')

    else:
        return render(request, 'users/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('input_data')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('index')
    else:
        return render(request, 'users/login.html')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')