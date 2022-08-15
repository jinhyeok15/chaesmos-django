from django.shortcuts import render, redirect

# models
from users.models import UserSession

# cookie
from commons.cookies import USER_SESSION_COOKIE_KEY

# view names
from commons.views import (
    INDEX_VIEW_NAME,
    SUCCESS_VIEW_NAME
)


def index(request):
    context = {'view_name': INDEX_VIEW_NAME}
    session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

    if session_id is None:
        context['is_logined'] = False
    context['is_logined'] = UserSession.objects.is_valid(session_id)

    return render(request, 'index.html', context)


def success(request):
    context = {'view_name': SUCCESS_VIEW_NAME}
    session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

    if session_id is None:
        context['is_logined'] = False
    context['is_logined'] = UserSession.objects.is_valid(session_id)

    return render(request, 'success.html', context)
