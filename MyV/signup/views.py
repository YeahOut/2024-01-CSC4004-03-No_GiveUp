from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UploadMAXMIN, MaxminNote
from .maxmin import maxAnalysis, minAnalysis
from .forms import SignupForm, PreferencesForm
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User,UserPreferences
from django.contrib.auth.decorators import login_required

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
            return redirect('signup4')  # 'next_step'은 다음 단계의 URL name입니다.
    else:
        form = PreferencesForm()
    return render(request, 'preferences_form.html', {'form': form})


class CustomSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('signup4')

def signup4(request):
    return render(request, 'signup/signup4.html')

# Create your views here.
def signup1(request):
    return render(request, 'account/signup.html')

@login_required
def signup2(request):
    return render(request, 'signup/signup2.html')

def signup3(request):
    return render(request, 'signup/signup3.html')

#S3에 파일 업로드하기
def upload_view(request):
    if request.method == 'POST':
        max_file = request.FILES.get('max_file', None)
        min_file = request.FILES.get('min_file', None)

        if max_file:
            new_name = 'max_' + max_file.name  # 파일 이름 앞에 max_붙이기
            max_file.name = new_name

            upload = UploadMAXMIN(max_file=max_file)
            upload.save()  # 모델 저장하기 (필수!)

        if min_file:
            new_name = 'min_' + min_file.name
            # 파일 이름 앞에 min_붙이기 (사용자마다 구분할 수 있도록 사용자 아이디도 앞에 추가해야할 것 같다.)
            min_file.name = new_name

            upload = UploadMAXMIN(min_file=min_file)
            upload.save()
            return HttpResponse("Files uploaded successfully")

    return HttpResponse("Failed to upload files")

