import boto3
import tempfile #임시로 파일 다운 받고 삭제하기 위해 사용
import os
##음원처리 위한 라이브러리
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
from django.conf import settings
from spleeter.separator import Separator

def vocalAnalyze() :
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
    
    #s3 버킷에 있는 파일 다운로드 하기
    bucket_name = 'myv-aws-bucket'
    bucket = s3.Bucket(bucket_name)

    #파일 다운로드하기
    obj_file= 'vocalReportSource/비교대상음원_최고음_김동국.wav'
    save_file=os.getcwd()+'/media/비교대상음원_최고음_김동국.wav'
    bucket.download_file(obj_file,save_file)


def vocalAnalyze(bucket_name, key):
    # 임시 파일 생성
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        s3_client = boto3.client('s3')

        try:
            # S3 버킷에서 임시 파일로 다운로드
            s3_client.download_file(bucket_name, key, temp_file.name)
            print(f"파일이 성공적으로 다운로드되었습니다: {temp_file.name}")

            # 파일 처리 로직
            #process_file(temp_file.name)

        except Exception as e:
            print(f"파일 다운로드 중 오류 발생: {e}")


def process_file():
    # 반주 & 보컬 분리
    #spleet(org)
    #spleet(usr)
    separator = Separator('spleeter:5stems')
    #분리할 음원 파일 경로 만들기 
    audio_file = os.getcwd()+"/media/audio/kaze_younha_sliced.mp3"
    #분리할 음원의 경로를 전달해서, 음원 분리하고, 현재 디렉토리 (os.getcwd())에 분리한 음원 파일 폴더 생성하기 
    #이 폴더는 추후에 다 사용한 후에는 삭제가 되어야 한다. --> os.remove로 처리할 부분
    separator.separate_to_file(audio_file, os.getcwd())

    #os.getcwd()가 os.path.join base_dir와 동일한 역할
    org = os.path.join(settings.BASE_DIR, "kaze_younha_sliced/vocals")
    #->"kaze_younha_sliced/vocals" 이게 sperator로 분리해서 만들어진 폴더/vocals(자체 생성하는 보컬파일 이름)의 경로 (확장자 제외)
    usr = os.path.join(settings.BASE_DIR, "media/audio", "kaze_mine")

    plt.figure(figsize=(12, 4))
    print("#################분리완#################")
    org_name = org + ".wav" #librosa에서 돌릴 음원파일의 경로 (즉 분리된 음원 이름까지 경로를 가져오고, wav를 붙여서 확장자 변경)
    usr_name = usr + ".wav"
    
    ##리브로사 분석 시작##
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

    print("#################제거완료#################")
    #os.remove(os.getcwd()+'/kaze_younha_sliced')

    print("사용자가 부른 부분은 음원의 {}초부터 입니다".format(int(t0)))
    print("점수 :", int(score * 100))
    print("최고음 :", max_note)
    print("최저음 :", min_note)
    print("가장 잘부른 구간 : {:.1f}초 ~ {:.1f}초".format(best_st, best_ed))
    #plt.show()
    return max_note, min_note, int(t0), best_st, best_ed

def spleet(org_file_name):
    if (os.path.isfile("./output")):
        shutil.rmtree("./output")
    stems = 5
    file_name = org_file_name

    spl = r'spleeter separate -p spleeter:' + \
          str(stems) + r'stems -o output ' + file_name + '.mp3'
    os.system(spl)

    src = os.path.join(settings.BASE_DIR, 'modal/output') + file_name + "/vocals.wav"
    dst = os.path.join(settings.BASE_DIR, 'modal')
    shutil.copy2(src, dst)
    shutil.rmtree(os.path.join(settings.BASE_DIR, 'modal/output'))
    if (os.path.isfile(file_name + ".wav")):
        os.remove(file_name + ".wav")
    os.rename("vocals.wav", file_name + ".wav")

def get_start_pos(f1_org, f1_usr, t_org, t_usr):
    # 두 함수 미분
    f1_org = np.gradient(f1_org)
    f1_usr = np.gradient(f1_usr)

    max_val = -sys.maxsize
    max_idx = 0
    len_org = len(f1_org)
    len_usr = len(f1_usr)

    # 슬라이딩 윈도우
    for i in range(0, len_org - len_usr):
        tmp_val = 0
        for j in range(0, len_usr):
            tmp_val += f1_org[i + j] * f1_usr[j]
        if (tmp_val > max_val):
            max_val = tmp_val
            max_idx = i

    t0 = t_org[max_idx]
    return t_usr, t0, max_idx


def accuracy_analysis(t_usr, idx, f0_org, f0_usr):
    track_len = len(f0_usr)
    f0_org = f0_org[idx:idx + track_len]

    # get score, min, max note
    min_hz = 10000
    max_hz = -1
    for i in range(0, track_len):
        if ~np.isnan(f0_usr[i]):
            if 100 < f0_usr[i] < 2000:
                min_hz = min(min_hz, f0_usr[i])
                max_hz = max(max_hz, f0_usr[i])

    min_note = librosa.hz_to_note(min_hz)
    max_note = librosa.hz_to_note(max_hz)
    cos_theta = (np.inner(f0_org, f0_usr) /
                 (math.sqrt(np.inner(f0_org, f0_org)) * math.sqrt(np.inner(f0_usr, f0_usr))))
    score = (math.exp(cos_theta + 1) - 1) / (math.exp(2) - 1)

    # get best term
    best_idx = 0
    best_score = -1
    term_len = track_len // 5

    for i in range(0, track_len - term_len):
        cur_score = np.inner(f0_org[i:i + term_len - 1], f0_usr[i:i + term_len - 1])
        if (cur_score > best_score):
            best_score = cur_score
            best_idx = i

    # log->선형 스케일 변환
    f0_org = 1200 * (np.log2(f0_org / 440) + 3)
    f0_usr = 1200 * (np.log2(f0_usr / 440) + 3)
    min_hz = 1200 * (math.log2(min_hz / 440) + 3)
    max_hz = 1200 * (math.log2(max_hz / 440) + 3)

    for i in range(0, len(f0_org)):
        if f0_org[i] < 0:
            f0_org[i] = np.nan

    for i in range(0, len(f0_usr)):
        if f0_usr[i] < 0:
            f0_usr[i] = np.nan

    # plot
    plt.plot(t_usr, f0_org, color='orangered', label="비교 음원")
    plt.plot(t_usr, f0_usr, color='deepskyblue', label="사용자 음원")
    plt.axhline(max_hz, t_usr[0], t_usr[-1], color='lightskyblue', linestyle='--', label="최고음")
    plt.axhline(min_hz, t_usr[0], t_usr[-1], color='lightsalmon', linestyle='--', label="최저음")
    plt.fill_between(t_usr[best_idx:best_idx + term_len - 1],
                     f0_usr[best_idx:best_idx + term_len - 1], color='lawngreen', alpha=0.3, label="가장 정확한 구간")

    #plt.legend()
    plt.savefig('./vocal_report_graph.png', bbox_inches='tight', dpi=300)
    return score, min_note, max_note, best_idx

