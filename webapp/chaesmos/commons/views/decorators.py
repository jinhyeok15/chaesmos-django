from commons.views import *
from commons.cookies import USER_SESSION_COOKIE_KEY
from users.models import UserSession


def authorize(func):
    def wrapper(request, *args, **kwargs):
        context = {}
        session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

        if session_id is None:
            context['is_logined'] = False
            context['session'] = None
            context['user'] = None
        else:
            context['is_logined'] = UserSession.objects.is_valid(session_id)

            session = UserSession.objects.get(pk=session_id)
            context['session'] = session

            user = session.fk_user_account
            context['user'] = user

        return func(request, context, *args, **kwargs)

    return wrapper
