from django.shortcuts import render, redirect
from accounts.forms import AccountSignupForm
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    form = AccountSignupForm()
    if request.method == 'POST':
        form = AccountSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-index')
        else:
            raise ValidationError("invalid signup form")
    return render(request, 'signup.html', {'form': form})
