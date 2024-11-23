import librosa
import librosa.display
import librosa.feature
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np
import sys
import os, asyncio
from .models import UserMaxMinFile 
from .awsInMain import downloadFile
from .models import UserMaxMinNote
from asgiref.sync import sync_to_async
from pydub import AudioSegment

def maxminAnalyze(user):
    #####download from s3
    # userInfo = await sync_to_async(UserMaxMinFile.objects.filter(user=user).order_by('-id').first())#db에서 정보 가져오기
    userInfo = UserMaxMinFile.objects.filter(user=user).order_by('-id').first()
    min_file_name = userInfo.min_file_name
    max_file_name = userInfo.max_file_name
    print(min_file_name)
    #await sync_to_async(downloadFile(min_file_name,max_file_name))
    downloadFile(min_file_name, max_file_name)
    print("checkpoint")

    #####analyze
    min_file_path = os.path.join(os.getcwd(),'media','maxminSrc',min_file_name)
    max_file_path = os.path.join(os.getcwd(),'media','maxminSrc',max_file_name)
    max_note = usingLibrosa_max(max_file_path, user)
    min_note = usingLibrosa_min(min_file_path, user)
    #print(min_note_fromMin, max_note_fromMax)

    #delete
    os.remove(min_file_path)
    os.remove(max_file_path)
    print("delete success")
    ###

    #####upload to user DB 
    upload = UserMaxMinNote(user = user, 
                   max_note = max_note,
                   min_note = min_note)
    #await sync_to_async(upload.save())
    upload.save()


def usingLibrosa_max(min_file_name, user):
    usrmax_convert_format(user)
    print("max convert success")
    y, sr = librosa.load(min_file_name)
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

    return max_note

def usingLibrosa_min(min_file_name, user):
    usrmin_convert_format(user)
    print("min onvert success")
    y, sr = librosa.load(min_file_name)
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
    min_note = librosa.hz_to_note(min_freq)

    return min_note

#최고음 확장자 처리
def usrmax_convert_format(user):
    is_usr_m4a = False
    is_usr_mp3 = False
    username=user
    username=str(username) 

    if (os.path.isfile(os.path.join(os.getcwd(), 'media',username,'_max.m4a'))):
        is_usr_m4a = True
    elif (os.path.isfile(os.path.join(os.getcwd(), 'media',username,'_max.mp3'))):
        is_usr_mp3 = True

    if(is_usr_m4a):
        org_audio = AudioSegment.from_file(os.path.join(os.getcwd(), 'media', username, '_max.m4a'), format="m4a")
        org_audio.export(os.path.join(os.getcwd(), 'media',username,'_max.wav'), format="wav")
    elif(is_usr_mp3) :
        org_audio = AudioSegment.from_file(os.path.join(os.getcwd(), 'media', username, '_max.mp3'), format="m4a")
        org_audio.export(os.path.join(os.getcwd(), 'media',username,'_max.wav'), format="wav")


#최저음 확장자 처리
def usrmin_convert_format(user):
    is_usr_m4a = False
    is_usr_mp3 = False
    username=user
    username=str(username)
    
    if (os.path.isfile(os.path.join(os.getcwd(), 'media',username,'_min.m4a'))):
        is_usr_m4a = True
    elif (os.path.isfile(os.path.join(os.getcwd(), 'media',username,'_min.mp3'))):
        is_usr_mp3 = True

    if(is_usr_m4a):
        org_audio = AudioSegment.from_file(os.path.join(os.getcwd(), 'media', username, '_min.m4a'), format="m4a")
        org_audio.export(os.path.join(os.getcwd(), 'media',username,'_min.wav'), format="wav")
    elif(is_usr_mp3) :
        org_audio = AudioSegment.from_file(os.path.join(os.getcwd(), 'media', username, '_min.mp3'), format="m4a")
        org_audio.export(os.path.join(os.getcwd(), 'media',username,'_min.wav'), format="wav")