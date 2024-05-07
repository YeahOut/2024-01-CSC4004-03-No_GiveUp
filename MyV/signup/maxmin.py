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

def maxAnalysis(sound):
    y, sr = librosa.load(sound)
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
    return max_note

def minAnalysis(sound):
    y, sr = librosa.load(f"{sound}")
    f0, voiced_flag, voiced_prob = librosa.pyin(y=y, fmin=60, fmax=2000, sr=sr)
    max_freq = -1
    min_freq = 3000
    sum_freq = 0
    valid_frame_cnt = 0
    for i in range(len(f0)):
        if (voiced_flag[i]):
            sum_freq += f0[i]
            min_freq = min(min_freq, f0[i])
            valid_frame_cnt += 1
    min_note = librosa.hz_to_note(max_freq)
    return min_note
