from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class AccountSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account

    def save(self, commit=True):
        account = super().save(commit=False)
        if commit:
            account.save()
        return account
