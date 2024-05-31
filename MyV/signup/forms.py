from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .validators import validate_no_special_characters

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "nickname", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 사용중인 이메일입니다!")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 사용중인 아이디입니다!")
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("이미 사용중인 닉네임입니다!")
        return nickname

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.nickname = self.cleaned_data['nickname']
        user.save()

class PreferencesForm(forms.Form):
    mood = forms.IntegerField(min_value=0, max_value=10)
    energy = forms.IntegerField(min_value=0, max_value=10)
    tempo = forms.IntegerField(min_value=0, max_value=10)
