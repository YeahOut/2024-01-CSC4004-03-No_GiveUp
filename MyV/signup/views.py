from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from allauth.account.views import SignupView
from .forms import SignupForm, PreferencesForm
from .models import User, UserPreferences

class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('signup4')

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(self.request)
            form.signup(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

@login_required
def save_preferences(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preferences = UserPreferences(
                user=request.user,
                mood=form.cleaned_data['mood'],
                energy=form.cleaned_data['energy'],
                tempo=form.cleaned_data['tempo']
            )
            preferences.save()
            return redirect('signup4')
    else:
        form = PreferencesForm()
    return render(request, 'preferences_form.html', {'form': form})

def signup4(request):
    return render(request, 'signup/signup4.html')

def signup1(request):
    return render(request, 'account/signup.html')

@login_required
def signup2(request):
    return render(request, 'signup/signup2.html')

def signup3(request):
    return render(request, 'signup/signup3.html')

