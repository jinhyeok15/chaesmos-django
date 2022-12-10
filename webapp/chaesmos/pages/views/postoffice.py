from django.shortcuts import render, redirect
from django.db import transaction

# models
from postoffice.models import DailyPost, Letter

# forms
from postoffice.forms import LetterCreateForm

# serializers
from postoffice.serializers import LetterListSerializer

# commons
from commons.views import (
    SUCCESS_VIEW_NAME, 
    WRITE_VIEW_NAME, 
    SOLVE_VIEW_NAME, 
    READ_LETTERS_VIEW_NAME,
    READ_LETTER_VIEW_NAME
)
from commons.views.decorators import authorize

# utils
from django.utils import timezone
from datetime import timedelta


@authorize
def write(request, context):
    context['view_name'] = WRITE_VIEW_NAME

    if request.method == 'POST':
        session = context['session']
        user = session.fk_user_account
        form = LetterCreateForm({
            'title': request.POST.get('title'),
            'main': request.POST.get('main'),
            'selected_date': request.POST.get('selected_date'),
            'fk_writer': user.id,
        })
        if form.is_valid():
            form.save()

        return redirect(SUCCESS_VIEW_NAME)
    else:
        form = LetterCreateForm()
    context['form'] = form
    return render(request, 'postoffice/write.html', context=context)


@authorize
def solve(request, context):  # POST는 REST_API로 처리
    context['view_name'] = SOLVE_VIEW_NAME

    user = context['user']

    if DailyPost.objects.is_expired(user):
        with transaction.atomic():
            letters = Letter.objects.rand_read(user)
            DailyPost.objects.generate(user, letters)
            context['letters'] = letters
    else:
        dailyposts = DailyPost.objects.filter(fk_reader=user, expired_at__range=(timezone.now(), timezone.now()+timedelta(days=1)))
        letters = [post.fk_letter for post in dailyposts] if dailyposts else []
        
        context['letters'] = letters

    context['letter_list'] = {'letters': LetterListSerializer(letters, many=True).data}
    
    return render(request, 'postoffice/solve.html', context=context)


@authorize
def read_letters(request, context):
    context['view_name'] = READ_LETTERS_VIEW_NAME

    user = context['user']
    letters = Letter.objects.filter(fk_writer=user)

    context['letters'] = letters
    context['detail'] = False

    return render(request, 'postoffice/my-mails.html', context=context)


@authorize
def read_letter(request, context, pk):
    context['view_name'] = READ_LETTER_VIEW_NAME

    obj = Letter.objects.get(pk=pk)

    context['letter'] = obj
    context['detail'] = True

    return render(request, 'postoffice/my-mail-detail.html', context=context)
