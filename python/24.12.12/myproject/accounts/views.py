from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib import messages

# 로그인 화면
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

# 회원가입 화면
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        vUsername = request.POST['username']
        vpassword1 = request.POST['password1']
        vpassword2 = request.POST['password2']
        
        print(f"Received POST data: username={vUsername}, password1={vpassword1}, password2={vpassword2}")

        if vpassword1 != vpassword2:
            messages.error(request, '패스워드가 일치하지 않습니다.')
            print("Passwords do not match.")
            return render(request, 'accounts/signup.html')

        if User.objects.filter(username=vUsername).exists():
            messages.error(request, '이미 존재하는 아이디입니다.')
            print("Username already exists.")
            return render(request, 'accounts/signup.html')

        user = User.objects.create_user(username=vUsername, password=vpassword1)
        user.save()
        print(f"User created: {user}")

        user = authenticate(username=vUsername, password=vpassword1)
        if user is not None:
            login(request, user)
            print("User authenticated and logged in.")
            return redirect('login')
        else:
            print("Authentication failed.")

    return render(request, 'accounts/signup.html');