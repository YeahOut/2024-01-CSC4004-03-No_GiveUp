from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
    
    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()
        
        
class PreferencesForm(forms.Form):
    mood = forms.IntegerField(min_value=0, max_value=10)
    energy = forms.IntegerField(min_value=0, max_value=10)
    tempo = forms.IntegerField(min_value=0, max_value=10)