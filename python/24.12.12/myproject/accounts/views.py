from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

# 로그인 화면
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("로그인성공")
            response = redirect('home')
            if remember_me:
                response.set_cookie('username', username, max_age=30*24*60*60)  # 30일 동안 쿠키 유지
            else:
                response.delete_cookie('username')
            return response
        else:
            print("user 가 없음")
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'accounts/login.html')

# 회원가입 ?
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


@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html');

def logout_view(request):
    logout(request)
    return redirect('login')