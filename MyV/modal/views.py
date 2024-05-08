from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UploadAnalyzeFile
# Create your views here.
def analyzePage(request):
    return render(request,'modal/analyze.html')

def upload_analyze_file(request):
    if request.method == 'POST':
        mySound_file = request.FILES.get('mysound_file', None)
        compareSound_file = request.FILES.get('comparesound_file', None)

        if mySound_file:
            new_name = '사용자음원_' + mySound_file.name  # 파일 이름 앞에 max_붙이기
            mySound_file.name = new_name

            upload = UploadAnalyzeFile(mySound_file=mySound_file)
            upload.save()  # 모델 저장하기 (필수!)

        if compareSound_file:
            new_name = '비교대상음원_' + compareSound_file.name
            # 파일 이름 앞에 min_붙이기 (사용자마다 구분할 수 있도록 사용자 아이디도 앞에 추가해야할 것 같다.)
            compareSound_file.name = new_name

            upload = UploadAnalyzeFile(compareSound_file=compareSound_file)
            upload.save()
            return HttpResponse("Files uploaded successfully")

    return HttpResponse("Failed to upload files")

def vocalResult(request):
    return render(request,'modal/analyze_result.html')