from django.shortcuts import render
from django.http import HttpResponse
from .vocal_report import spleet,get_start_pos,accuracy_analysis

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

# Create your views here.
def index(request):
    return render(request, 'myauth/intropage.html')

def team(request):
    return render(request, 'myauth/team.html')

#librosa 처리 후 렌더링 테스트
def maxminAnalysis(request):
    y, sr = librosa.load(librosa.ex('trumpet'))
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
    return render(request, 'myauth/sign_up_3.html', context)

#보컬분석 부분 처리하기

def vocalReport(request):
    org = "kaze_younha_sliced"
    usr = "kaze_mine"

    # 반주 & 보컬 분리
    #spleet(org)
    spleet(librosa.ex('trumpet'))
    # spleet(usr)

    plt.figure(figsize=(12, 4))
    #org_name = org + ".wav"
    #테스트차원에서 librosa 예시음원 사용하기
    org_name = librosa.ex('trumpet')
    #usr_name = usr + ".wav"
    usr_name = librosa.ex('trumpet')
    y_org, sr_org = librosa.load(org_name)
    y_usr, sr_usr = librosa.load(usr_name)
    f0_org, voiced_flag_org, voiced_prob_org = librosa.pyin(y=y_org, fmin=60, fmax=2000, sr=sr_org)
    f0_usr, voiced_flag_usr, voiced_prob_usr = librosa.pyin(y=y_usr, fmin=60, fmax=2000, sr=sr_usr)
    frames_org = range(len(f0_org))
    frames_usr = range(len(f0_usr))
    t_org = librosa.frames_to_time(frames_org)
    t_usr = librosa.frames_to_time(frames_usr)

    for i in range(0, len(f0_org)):
        if (np.isnan(f0_org[i])):
            f0_org[i] = -10000

    for i in range(0, len(f0_usr)):
        if (np.isnan(f0_usr[i])):
            f0_usr[i] = -10000

    f1_org = f0_org.copy()
    f1_usr = f0_usr.copy()

    t_usr, t0, idx = get_start_pos(f1_org=f0_org, f1_usr=f0_usr, t_org=t_org, t_usr=t_usr)

    score, min_note, max_note, best_idx = accuracy_analysis(t_usr, idx, f0_org, f0_usr)
    best_st = t_usr[best_idx]
    best_ed = t_usr[best_idx + len(f0_usr) // 5]

    # 템플릿에 넘길 데이터들
    context = {'startTime': int(t0), 'score':  int(score * 100),
               'max': max_note,'min':min_note,
               'best_st':best_st,'best_ed':best_ed}
    return render(request, 'myauth/result.html', context)