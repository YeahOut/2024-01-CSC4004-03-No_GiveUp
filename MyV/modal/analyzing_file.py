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
import plotly.graph_objects as go
from pydub import AudioSegment
from spleeter.separator import Separator

def process_file():
    # 반주 & 보컬 분리
    org = "org"
    usr = "usr"

    #확장자 예외처리
    org_convert_format()
    print("##확장자 예외처리 성공##")
    #usr_convert_format()

    # 반주 & 보컬 분리
    spleet(org)
    #spleet(usr)
    
    plt.figure(figsize=(12, 4))
    print("#################분리완#################")
    org_name = os.path.join(os.getcwd(),'media', 'vocalReportSrc', "org.wav") #librosa에서 돌릴 음원파일의 경로 (즉 분리된 음원 이름까지 경로를 가져오고, wav를 붙여서 확장자 변경)
    usr_name = os.path.join(os.getcwd(),'media', 'vocalReportSrc', "usr.wav") #librosa에서 돌릴 음원파일의 경로 (즉 분리된 음원 이름까지 경로를 가져오고, wav를 붙여서 확장자 변경)
    
    ##리브로사 분석 시작##
    y_org, sr_org = librosa.load(org_name)
    y_usr, sr_usr = librosa.load(usr_name)

    print(f"org 업로드 확인하기: {len(y_org)} samples at {sr_org} Hz")
    print(f"usr 업로드 확인하기: {len(y_usr)} samples at {sr_usr} Hz")

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
    print("###test1###")
    t_usr, t0, idx = get_start_pos(f1_org=f0_org, f1_usr=f0_usr, t_org=t_org, t_usr=t_usr)
    print("###test###")
    score, min_note, max_note, best_idx = accuracy_analysis(t_org, t_usr, idx, f0_org, f0_usr)
    print("###test###")
    best_st = t_usr[best_idx]
    best_ed = t_usr[best_idx + len(f0_usr) // 5]
    score = int(score *100)
    remove_prefiles()
    
    print("사용자가 부른 부분은 음원의 {}초부터 입니다".format(int(t0)))
    print("점수 :", int(score * 100))
    print("최고음 :", max_note)
    print("최저음 :", min_note)
    print("가장 잘부른 구간 : {:.1f}초 ~ {:.1f}초".format(best_st, best_ed))
    print("점수: score")
    #plt.show()
    return max_note, min_note, int(t0), best_st, best_ed, score

def spleet(org_file_name):
    output_dir = os.path.join(os.getcwd(), 'output') #output폴더를 생성할 경로 정해주기
    if (os.path.isfile(output_dir)):
        shutil.rmtree(output_dir)

    #os.makedirs(output_dir)#spleet 함수 쓸 경우 만들어야 하니까
    stems = 5
    file_path = os.path.join(os.getcwd(),'media','vocalReportSrc',org_file_name) #mp3파일이 있는 폴더로 파일명 정해주기 (확장자는 not yet) 
    file_name = org_file_name #그냥 파일명 org, usr 이렇게 
    spl = f'spleeter separate -p spleeter:{stems}stems -o "{output_dir}" "{file_path}.m4a"'
    os.system(spl)
    print("##check point1##")

    src = os.path.join(output_dir, file_name, "vocals.wav") #spleet 함수로 만든 vocal.wav 찾기
    dst = os.path.join(os.getcwd(), 'media', 'vocalReportSrc') #spleet 함수가 만든 vocal.wav 파일을 meida/vocalReportSrc로 옮기기 위한 도착 경로

    print("##check point2##")
    print("src: ", src) #for debug
    print("dst: ", dst) #for debug
    
    shutil.copy2(src, dst) #src voacl.wav copy to dst path
    print("##check point3##")

    shutil.rmtree(output_dir) #spleet 함수로 만든 Output 폴더 삭제하기
    print("##rmtree check point4##")

    if (os.path.isfile(file_name + ".wav")):
        os.remove(file_name + ".wav")
    os.rename(os.path.join(dst,"vocals.wav"), os.path.join(dst,"org.wav"))

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


def accuracy_analysis(t_org, t_usr, idx, f0_org, f0_usr):
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

    # plot update 0517
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t_org, y=f0_org, fill='tozeroy', name='비교 음원'))
    fig.add_trace(go.Scatter(x=t_usr, y=f0_usr, fill='tozeroy', name='사용자 음원'))
    fig.add_hline(y=max_hz, line_dash="dash", label=dict(text="최고음"))
    fig.add_hline(y=min_hz, line_dash="dash", label=dict(text="최저음"))
    fig.add_vrect(x0=t_usr[best_idx], x1=t_usr[best_idx+term_len-1], fillcolor='green',
                  opacity=0.25, line_width=0, label=dict(text="가장 정확한 구간"))
    fig.update_layout(legend_yanchor='top', legend_y=0.99, legend_xanchor='left', legend_x=0.01,
                      margin_l=0, margin_r=0, margin_b=0, margin_t=0)
    fig.write_image(os.path.join(os.getcwd(),'modal','static','modal','images','vocal_report_graph.png'))
    #fig.show()
    return score, min_note, max_note, best_idx

##0517 update
def org_convert_format():
    is_org_m4a = False
    if (os.path.isfile(os.path.join(os.getcwd(), 'media', 'org.m4a'))) :
        is_org_m4a = True

    if(is_org_m4a):
        org_audio = AudioSegment.from_file(os.path.join(os.getcwd(), 'media','org.m4a'), format="m4a")
        org_audio.export(os.path.join(os.getcwd(), 'media', 'org.mp3'), format="mp3")

def usr_convert_format():
    is_usr_m4a = False
    if (os.path.isfile(os.path.join(os.getcwd(), 'media','usr.m4a'))):
        is_usr_m4a = True

    if(is_usr_m4a):
        org_audio = AudioSegment.from_file(os.path.join(os.getcwd(), 'media', 'usr.m4a'), format="m4a")
        org_audio.export(os.path.join(os.getcwd(), 'media','usr.mp3'), format="mp3")

def remove_prefiles():
    if (os.path.isfile("org.wav")):
        os.remove("org.wav")
    if (os.path.isfile("org.mp3")):
        os.remove("org.mp3")
    if (os.path.isfile("org.m4a")):
        os.remove("org.m4a")
    if (os.path.isfile("usr.wav")):
        os.remove("usr.wav")
    if (os.path.isfile("usr.mp3")):
        os.remove("usr.mp3")
    if (os.path.isfile("usr.m4a")):
        os.remove("usr.m4a")
