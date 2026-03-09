from django.shortcuts import render,redirect

# Create your viefrom django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return redirect('login')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('create_task')   # FIXED
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

