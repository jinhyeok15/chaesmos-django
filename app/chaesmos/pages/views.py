from django.shortcuts import render, redirect
from users.forms import UserAccountSignUpForm, UserAccountLoginForm
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserAccountSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-index')
    else:
        form = UserAccountSignUpForm()

    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserAccountLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-index')
    else:
        form = UserAccountLoginForm()

    return render(request, 'login.html', {'form': form})
