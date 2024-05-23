from django.shortcuts import render,redirect
from django.http import HttpResponse
from .analyzing_file import process_file
from .aws import downloadFile, upload_to_s3, makingBucket,deleteBucket

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
        
        if mySound_file and compareSound_file:
            upload_to_s3(mySound_file, compareSound_file)
            return HttpResponse("Files uploaded successfully")
        else:
            return HttpResponse("Failed to upload files")
    
    return HttpResponse("Failed to upload files")


def vocalResult(request):
    #context = maxminAnalysis(request)
    downloaded = downloadFile() #음원 다운로드 받기
    print("##전달 성공##")

    if (downloaded==1):
        max_note, min_note, start_t, best_st, best_ed, score = process_file()
        context = {'max':max_note, 'min':min_note, 'start_t': start_t, 'best_st': int(best_st), 'best_ed':int(best_ed), 'score':score}
        #user = request.user  # 현재 로그인한 사용자에 접근하기 위한 용도..
        #saveInfo = UserVocalInfo(user= user, max_note=max_note, min_note=min_note)
        #saveInfo.save()
    else :
        print("##파일이 다운로드 되지 않았음##")
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