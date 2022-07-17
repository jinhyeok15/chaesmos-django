from django import forms
from .models import *

# exception
from django.core.exceptions import ValidationError


class UserAccountSignUpForm(forms.ModelForm):
    
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)
    password_again = forms.CharField(required=False)
    validate = forms.ChoiceField()

    class Meta:
        model = UserAccount
        fields = ["username", "password", "nickname"]
    
    def clean_username(self):
        username = self.data.get('username')
        user = UserAccount.objects.filter(username=username).first()

        if user is not None:
            raise ValidationError('이미 사용중인 아이디입니다.')
        
        return username
    
    def clean_nickname(self):
        nickname = self.data.get('nickname')
        user = UserAccount.objects.filter(nickname=nickname).first()

        if user is not None:
            raise ValidationError('이미 사용중인 닉네임입니다.')
        
        return nickname
    
    def clean_password(self):
        password = self.data.get('password')
        password_again = self.data.get('password_again')

        if password != password_again:
            raise ValidationError('비밀번호가 일치하지 않습니다.')
        
        return password


class UserAccountLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def save(self):
        data = self.data
        username = data.get('username')
        user = UserAccount.objects.get(username=username)

        return UserSession.objects.create(fk_user_account=user)
    
    def is_valid(self):
        data = self.data
        username = data.get('username')
        password = data.get('password')
        user = UserAccount.objects.login_user(username=username, password=password)

        if user is None:
            self.add_error(None, '아이디 혹은 비밀번호가 일치하지 않습니다.')
            return False
        return True
