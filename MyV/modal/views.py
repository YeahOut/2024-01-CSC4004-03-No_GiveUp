from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UploadAnalyzeFile
from .analyzing_file import process_file
# Create your views here.

from django.conf import settings
import librosa
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

# def analyze_ing(request):
#     # 사용 예:
#     # bucket = 'myv-aws-bucket'
#     # key = 'vocalReportSource/비교대상음원_최고음_김동국.wav'
#     # vocalAnalyze(bucket, key)
#     process_file()
#     return render(request,'modal/analyze_ing.html')

def vocalResult(request):
    #context = maxminAnalysis(request)
    max_note, min_note, start_t, best_st, best_ed = process_file()
    context = {'max':max_note, 'min':min_note, 'start_t': start_t, 'best_st':best_st, 'best_ed':best_ed}
    return render(request, 'modal/analyze_result.html', context)



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