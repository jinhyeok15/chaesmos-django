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

# decorators
from commons.views.decorators import authorize

# view names
from commons.views import (
    INDEX_VIEW_NAME,
    LOGIN_VIEW_NAME,
    SIGNUP_VIEW_NAME,
    LOGOUT_VIEW_NAME,
)

# Create your views here.


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


@authorize
def logout(request, context):
    session = context['session']
    if session:
        session.delete()
    else:
        return ValidationError('session이 존재하지 않습니다.')

    http = redirect(INDEX_VIEW_NAME)
    http.delete_cookie(USER_SESSION_COOKIE_KEY)

    return http
