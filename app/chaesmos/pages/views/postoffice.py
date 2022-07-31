from xml.dom import ValidationErr
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.db import transaction

# models
from users.models import UserAccount, UserSession

# forms
from postoffice.forms import LetterCreateForm

# commons
from commons.views import WRITE_VIEW_NAME, COMMENT_VIEW_NAME, INDEX_VIEW_NAME

# cookies
from commons.cookies import USER_SESSION_COOKIE_KEY


def write(request):
    context = {'view_name': WRITE_VIEW_NAME}
    session_id = request.COOKIES.get(USER_SESSION_COOKIE_KEY)

    if session_id is None:
        context['is_logined'] = False
    context['is_logined'] = UserSession.objects.is_valid(session_id)
    
    if request.method == 'POST':
        session = UserSession.objects.get(pk=session_id)
        user = session.fk_user_account
        form = LetterCreateForm({
            'title': request.POST.get('title'),
            'main': request.POST.get('main'),
            'selected_date': request.POST.get('selected_date'),
            'fk_writer': user.id,
        })
        if form.is_valid():
            form.save()

        return redirect(INDEX_VIEW_NAME)
    else:
        form = LetterCreateForm()
    context['form'] = form
    return render(request, 'postoffice/write.html', context=context)

def comment(request):
    return
