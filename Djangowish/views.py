from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'accounts/login.html')

@login_required
def choice(request):
    return render(request, "choice.html")

@login_required
def bdayinput(request):
    return  render(request, 'bday/bdayinput.html')

@login_required
def vdayinput(request):
    return render(request, 'vday/vdayinput.html')

@login_required
def mylogout(request):
    logout(request)
    return redirect('login')




