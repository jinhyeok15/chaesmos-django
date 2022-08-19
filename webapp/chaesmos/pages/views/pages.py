from django.shortcuts import render, redirect

# view names
from commons.views import (
    INDEX_VIEW_NAME,
    SUCCESS_VIEW_NAME
)

# models
from users.models import UserSession

# commons
from commons.cookies import USER_SESSION_COOKIE_KEY

# decorators
from commons.views.decorators import authorize


# index는 auth 검증 필요 x
def index(request):
    context = {'view_name': INDEX_VIEW_NAME}
    session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

    if session_id is None:
        context['is_logined'] = False
    context['is_logined'] = UserSession.objects.is_valid(session_id)

    return render(request, 'index.html', context)


@authorize
def success(request, context):
    context['view_name'] = SUCCESS_VIEW_NAME

    return render(request, 'success.html', context)
