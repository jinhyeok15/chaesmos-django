from xml.dom import ValidationErr
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.db import transaction

# models
from users.models import UserAccount, UserSession

# forms
from postoffice.forms import LetterCreateForm

# commons
from commons.views import LETTER_VIEW_NAME, COMMENT_VIEW_NAME

# cookies
from commons.cookies import USER_SESSION_COOKIE_KEY


def letter(request):
    if request.method == 'POST':
        session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)
        if not UserSession.objects.is_valid(session_id):
            raise ValidationError("세션이 만료되었습니다.")
        session = UserSession.objects.get(pk=session_id)
        user = session.fk_account_user

        form = LetterCreateForm({
            **request.POST,
            'fk_writer': user
        })
        if form.is_valid():
            form.save()
    else:
        form = LetterCreateForm()
    return render(request, 'postoffice/letter.html', {
        'form': form
    })

def comment(request):
    return
