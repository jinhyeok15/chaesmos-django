from django.core.exceptions import ValidationError
from rest_framework.views import APIView

from commons.views.response import (
    GenericResponse as Response,
    HttpStatus
)
from commons.cookies import USER_SESSION_COOKIE_KEY

# mixins
from commons.views.mixin import GenericMixin

# Create your views here.


class UserLogout(GenericMixin, APIView):

    def post(self, request):
        from .models import UserSession

        session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)
        try:
            session = UserSession.objects.get(pk=session_id)
            session.delete()

            return Response(None, HttpStatus(200))
        except UserSession.DoesNotExist:
            e = ValidationError('session invalid')
            return Response(None, HttpStatus(400, error=e))
