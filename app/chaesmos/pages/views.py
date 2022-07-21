from django.shortcuts import render, redirect
from django.db import transaction

# models
from users.models import UserSession

# forms
from users.forms import UserAccountSignUpForm, UserAccountLoginForm

# exceptions
from django.core.exceptions import ValidationError

# cookie
from commons.cookies import USER_SESSION_COOKIE_KEY
from commons.views import (
    INDEX_VIEW_NAME,
    LOGIN_VIEW_NAME,
    SIGNUP_VIEW_NAME,
)

# Create your views here.


def index(request):
    context = {'view_name': INDEX_VIEW_NAME}
    session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

    if session_id is None:
        context['is_logined'] = False
    context['is_logined'] = UserSession.objects.is_valid(session_id)

    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserAccountSignUpForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                session = UserSession.objects.create(fk_user_account=user)
                http = redirect(INDEX_VIEW_NAME)
                http.set_cookie(USER_SESSION_COOKIE_KEY, session.id)
                return http
    else:
        form = UserAccountSignUpForm()

    return render(request, 'users/signup.html', {
        'form': form, 
        'submit_value': '회원가입하기',
        'view_name': SIGNUP_VIEW_NAME,
    })


def login(request):
    if request.method == 'POST':
        form = UserAccountLoginForm(request.POST)
        if form.is_valid():
            session = form.save()
            http = redirect(INDEX_VIEW_NAME)
            http.set_cookie(USER_SESSION_COOKIE_KEY, session.id)

            return http
    else:
        form = UserAccountLoginForm()

    return render(request, 'users/login.html', {
        'form': form, 
        'submit_value': '로그인',
        'view_name': LOGIN_VIEW_NAME,
    })
