from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def redirect_to_login(request):
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')