from django.shortcuts import render, redirect
from django.db import transaction

# models
from postoffice.models import DailyPost, Letter

# forms
from postoffice.forms import LetterCreateForm

# serializers
from postoffice.serializers import LetterListSerializer

# commons
from commons.views import SUCCESS_VIEW_NAME
from commons.views.decorators import authorize


@authorize
def write(request, context):
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
def solve(request, context):
    user = context['user']

    if DailyPost.objects.is_expired(user):
        with transaction.atomic():
            letters = Letter.objects.rand_read(user)
            DailyPost.objects.generate(user, letters)
            context['letters'] = letters
    else:
        dailyposts = DailyPost.objects.filter(fk_reader=user)
        letters = [post.fk_letter for post in dailyposts] if dailyposts else []
        
        context['letters'] = letters

    context['letter_list'] = {'letters': LetterListSerializer(letters, many=True).data}
    
    return render(request, 'postoffice/solve.html', context=context)


@authorize
def read_letters(request, context):
    user = context['user']
    letters = Letter.objects.filter(fk_writer=user)
    print(letters)

    return render(request, 'postoffice/my-mails.html', context=context)
