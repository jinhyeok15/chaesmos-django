from django import forms
from .models import *
from django.db.models import Q
from django.core.exceptions import ValidationError


class UserAccountSignUpForm(forms.ModelForm):
    
    password_again = forms.CharField()

    class Meta:
        model = UserAccount
        fields = ["username", "password", "nickname"]

    def is_valid(self):
        data = self.data
        if self.is_existed(data.get('username'), data.get('nickname')):
            return False
        if data['password'] != data['password_again']:
            return False
        return True
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = UserAccount.objects.filter(username=username).first()

        if user is not None:
            raise ValidationError('이미 사용중인 아이디입니다.')
        
        return username
    
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        user = UserAccount.objects.filter(nickname=nickname).first()

        if user is not None:
            raise ValidationError('이미 사용중인 닉네임입니다.')


class UserAccountLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def save(self):
        data = self.data
        username = data.get('username')
        password = data.get('password')
        user = UserAccount.objects.filter(username=username, password=password).first()

        return UserSession.objects.create(fk_user_account=user)
    
    def is_valid(self):
        data = self.data
        username = data.get('username')
        password = data.get('password')
        user = UserAccount.objects.filter(username=username, password=password).first()

        if user is None:
            self.add_error(None, '아이디 혹은 비밀번호가 일치하지 않습니다.')
            return False
        return True
