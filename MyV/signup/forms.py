from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'user_ID', 'user_mood', 'user_energy', 'user_tempo']


    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.user_ID = self.cleaned_data['user_ID']
        user.user_mood = self.cleaned_data['user_mood']
        user.user_energy = self.cleaned_data['user_energy']
        user.user_tempo = self.cleaned_data['user_tempo']
        user.save()
        return user
