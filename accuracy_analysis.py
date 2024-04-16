import librosa
import librosa.display
import librosa.feature
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import shutil

def spleet(org_file_name):
    if(os.path.isfile("./output")):
        shutil.rmtree("./output")
    stems = 5
    path = "./"
    file_name = org_file_name

    spl = r'spleeter separate -p spleeter:' + \
          str(stems) + r'stems -o output ' + file_name + '.mp3'
    os.system(spl)

    src = "./output/" + file_name + "/vocals.wav"
    dst = "./"
    shutil.copy2(src, dst)
    shutil.rmtree("./output")
    if (os.path.isfile(file_name + ".wav")):
        os.remove(file_name + ".wav")
    os.rename("vocals.wav", file_name + ".wav")

def get_start_pos(f1_org, f1_usr):

    for i in range(0, len(f1_org)):
        if(np.isnan(f1_org[i])):
            f1_org[i] = -10000

    for i in range(0, len(f1_usr)):
        if(np.isnan(f1_usr[i])):
            f1_usr[i] = -1000

    frames_org = range(len(f1_org))
    frames_usr = range(len(f1_usr))
    t_org = librosa.frames_to_time(frames_org)
    t_usr = librosa.frames_to_time(frames_usr)

    #두 함수 미분
    f1_org = np.gradient(f1_org)
    f1_usr = np.gradient(f1_usr)

    max_val = -sys.maxsize
    max_idx = 0
    len_org = len(f1_org)
    len_usr = len(f1_usr)

    #슬라이딩 윈도우
    for i in range(0, len_org - len_usr):
        tmp_val = 0
        for j in range(0, len_usr):
            tmp_val += f1_org[i + j] * f1_usr[j]
        if(tmp_val > max_val):
            max_val = tmp_val
            max_idx = i

    t0 = t_org[max_idx]
    return t_usr, t0, max_idx

def accuracy_analysis(t_usr, idx, f0_org, f0_usr):
    l = len(f0_usr)
    f0_org = f0_org[idx:idx+l]
    
    #log->선형 스케일 변환
    f0_org = 1200 * (np.log2(f0_org/440) + 3)
    f0_usr = 1200 * (np.log2(f0_usr/440) + 3)
    
    result = f0_usr - f0_org

    plt.subplot(211)
    plt.plot(t_usr, result, 'b')
    plt.axhline(y=0, color='r')

    plt.subplot(212)
    plt.plot(t_usr, f0_org, 'r')
    plt.plot(t_usr, f0_usr, 'b')
    plt.show()

if __name__ == "__main__":

    org = "kaze_younha"
    usr = "kaze_mine"

    #반주 & 보컬 분리
    spleet(org)

    plt.figure(figsize=(20, 6))
    org_name = org + ".wav"
    usr_name = usr + ".wav"
    y_org, sr_org = librosa.load(org_name)
    y_usr, sr_usr = librosa.load(usr_name)
    y_org = y_org[:len(y_org) // 2]
    f0_org, voiced_flag_org, voiced_prob_org = librosa.pyin(y=y_org, fmin=60, fmax=2000, sr=sr_org)
    f0_usr, voiced_flag_usr, voiced_prob_usr = librosa.pyin(y=y_usr, fmin=60, fmax=2000, sr=sr_usr)

    f1_org = f0_org.copy()
    f1_usr = f0_usr.copy()
    t_usr, t0, idx = get_start_pos(f1_org=f1_org, f1_usr=f1_usr)

    print("사용자가 부른 부분은 음원의", t0, "초부터입니다")

    accuracy_analysis(t_usr, idx, f0_org, f0_usr)
