from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UploadMAXMIN
# Create your views here.
def signup1(request):
    return render(request, 'signup/signup1.html')

def signup2(request):
    return render(request, 'signup/signup2.html')

def signup3(request):
    return render(request, 'signup/signup3.html')

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
            new_name = 'min_' + min_file.name # 파일 이름 앞에 min_붙이기
            min_file.name = new_name

            upload = UploadMAXMIN(min_file=min_file)
            upload.save()

            return HttpResponse("Files uploaded successfully")

    return HttpResponse("Failed to upload files")