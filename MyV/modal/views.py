from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UploadAnalyzeFile
from .analyzing_file import process_file, downloadFile
# Create your views here.

from django.conf import settings
import librosa, boto3
import librosa.display
import librosa.feature
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np
import sys
import os
import shutil
import math

def analyzePage(request):
    return render(request,'modal/analyze.html')

#AWS s3에 업로드하는 함수
def upload_analyze_file(request):
    if request.method == 'POST':
        mySound_file = request.FILES.get('mysound_file', None)
        compareSound_file = request.FILES.get('comparesound_file', None)
        
        new_name = '사용자음원_' + mySound_file.name  # 파일 이름 앞에 max_붙이기
        mySound_file.name = new_name
    
        
        new_name = '비교대상음원_' + compareSound_file.name
            # 파일 이름 앞에 min_붙이기 (사용자마다 구분할 수 있도록 사용자 아이디도 앞에 추가해야할 것 같다.)
        compareSound_file.name = new_name

        upload = UploadAnalyzeFile(mySound_file=mySound_file,
                                   fMySound_name=mySound_file.name,
                                   compareSound_file=compareSound_file, 
                                   fCompareSound_name=compareSound_file.name)
        upload.save()
        return HttpResponse("Files uploaded successfully")
    
    return HttpResponse("Failed to upload files")


def vocalResult(request):
    #context = maxminAnalysis(request)
    downloaded = downloadFile(mineSound, compareSound) #음원 다운로드 받기
    print("##전달 성공##")

    if (downloaded==1):
        max_note, min_note, start_t, best_st, best_ed = process_file()
        context = {'max':max_note, 'min':min_note, 'start_t': start_t, 'best_st':best_st, 'best_ed':best_ed}
    return render(request, 'modal/analyze_result.html', context)


##views.py로 바로 확인하기 위한 함수 >> analyzing_file.py에서 활용할 예정
def downloadFile(request):
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
    
    #s3 버킷 정보 가져오기
    bucket_name = 'myv-aws-bucket'
    bucket = s3.Bucket(bucket_name)
    print("###test###")
    print(bucket)

    #파일 다운로드 진행하기
    obj_file= 'vocalReportSource/사용자음원_kaze_mine.wav' #디렉토리 버킷 접근하기
    userName = '김지민'
    mysound = '비교대상음원_최고음_'+userName+'.wav' #버킷에서 다운로드 할 파일 이름을 다운할 때 바꿀 수 있는데, 그 부분임.
    save_file = os.path.join(os.getcwd(), 'media', 'vocalReportSrc', mysound) #저장위치 및 파일 이름 설정
    bucket.download_file(obj_file,save_file)
    return HttpResponse("download 성공~")


#로컬에 있는 음원으로 최고최저 분석하는 함수
def maxminAnalysis(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'audio', 'kaze_mine.wav')
    y, sr = librosa.load(file_path)
    # y = y[:len(y) // 2]
    f0, voiced_flag, voiced_prob = librosa.pyin(y=y, fmin=60, fmax=2000, sr=sr)

    max_freq = -1
    min_freq = 3000
    sum_freq = 0
    valid_frame_cnt = 0
    for i in range(len(f0)):
        if (voiced_flag[i]):
            sum_freq += f0[i]
            max_freq = max(max_freq, f0[i])
            min_freq = min(min_freq, f0[i])
            valid_frame_cnt += 1
    max_note = librosa.hz_to_note(max_freq)
    min_note = librosa.hz_to_note(min_freq)
    avg_note = librosa.hz_to_note(sum_freq / valid_frame_cnt)

    context = {'max': max_note, 'min': min_note, 'avg':avg_note}  # 템플릿에 넘길 데이터를 사전형으로 만들기
    return context