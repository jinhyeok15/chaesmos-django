from django.core.exceptions import ValidationError
from rest_framework.views import APIView

# models
from users.models import UserSession
from postoffice.models import Solution, Letter, DailyPost

from django.db import transaction

# serializer
from postoffice.serializers import SolutionSerializer

# commons
from commons.views.response import (
    GenericResponse as Response,
    HttpStatus
)
from commons.cookies import USER_SESSION_COOKIE_KEY

# mixins
from commons.views.mixin import GenericMixin

# Create your views here.


class SolutionView(APIView, GenericMixin):
    def post(self, request):
        session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

        if session_id is None:
            return Response(None, HttpStatus(401))

        session = UserSession.objects.get(pk=session_id)
        user = session.fk_user_account

        letter_id = request.data.get('letter')
        
        try:
            letter = Letter.objects.get(pk=letter_id)
        except Letter.DoesNotExist:
            return Response(None, HttpStatus(404))

        with transaction.atomic():
            solution = Solution.objects.create(
                fk_letter=letter,
                fk_sender=user,
                main=request.data.get('main')
            )

            # delete DailyPost because you already send solution
            DailyPost.objects.filter(fk_letter=letter, fk_reader=user).delete()

        return Response(SolutionSerializer(solution).data, HttpStatus(200))
