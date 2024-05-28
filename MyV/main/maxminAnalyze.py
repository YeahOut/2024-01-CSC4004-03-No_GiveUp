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
from .models import UserMaxMinFile 
from .awsInMain import downloadFile
from .models import UserMaxMinNote
from asgiref.sync import sync_to_async


@sync_to_async
def maxminAnalyze(user):
    #####download from s3
    userInfo = UserMaxMinFile.objects.filter(user=user).order_by('-id').first() #db에서 정보 가져오기
    min_file_name = userInfo.min_file_name
    max_file_name = userInfo.max_file_name
    #print(min_file_name)
    downloadFile(min_file_name,max_file_name)
    #print("checkpoint")

    #####analyze
    min_file_path = os.path.join(os.getcwd(),'media','maxminSrc',min_file_name)
    max_file_path = os.path.join(os.getcwd(),'media','maxminSrc',max_file_name)
    max_note_fromMin, min_note_fromMin = usingLibrosa(min_file_path)
    max_note_fromMax, min_note_fromMax = usingLibrosa(max_file_path)
    #print(min_note_fromMin, max_note_fromMax)

    #####upload to user DB 
    upload = UserMaxMinNote(user = user, 
                   max_note = max_note_fromMax,
                   min_note = min_note_fromMin)
    upload.save()

    os.remove(min_file_path)
    os.remove(max_file_path)

@sync_to_async
def usingLibrosa(min_file_name):
    y, sr = librosa.load(min_file_name)
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

    return max_note, min_note