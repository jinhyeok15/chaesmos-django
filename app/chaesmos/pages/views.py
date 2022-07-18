from django.shortcuts import render, redirect
from users.forms import UserAccountSignUpForm, UserAccountLoginForm
from django.core.exceptions import ValidationError

# Create your views here.

USER_SESSION_COOKIE_KEY = 'user_session_id'

def index(request):
    session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)
    print('-----------',session_id)
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserAccountSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-index')
    else:
        form = UserAccountSignUpForm()

    return render(request, 'users/signup.html', {'form': form, 'submit_value': '회원가입하기'})


def login(request):
    if request.method == 'POST':
        form = UserAccountLoginForm(request.POST)
        if form.is_valid():
            session = form.save()
            http = redirect('page-index')
            http.set_cookie(USER_SESSION_COOKIE_KEY, session.id)

            return http
    else:
        form = UserAccountLoginForm()

    return render(request, 'users/login.html', {'form': form, 'submit_value': '로그인'})
