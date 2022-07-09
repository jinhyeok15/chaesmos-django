from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Account


class AccountSignupForm(UserCreationForm):
    username = forms.CharField(label='닉네임', min_length=2, max_length=15)
    email = forms.EmailField(label='이메일')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재확인', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = Account

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = Account.objects.filter(username = username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = Account.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit = True):
        user = Account.objects.create_user(
            self.username_clean(),
            self.email_clean(),
            self.clean_password2()
        )
        return user
