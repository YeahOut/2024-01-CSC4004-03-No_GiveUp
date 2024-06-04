# 2024-01-CSC4004-03-No_GiveUp

2024-1 공개 SW 프로젝트 3분반 7조 &lt;포7l를 모르조 >의 레포입니다.

<br><br>

# 🎵 사용자 음역대 분석 및 노래 추천 웹 서비스, MyV

- 배포 링크 :
- Test ID :
- Test PW :

  <br>

---

## 👩🏻‍🏫 프로젝트 소개

- LIBROSA 라이브러리 기반 **사용자** 최고음, 최저음, 음역대, **성향을 기반**으로 정보를 분석
- 사용자의 목소리를 분석하여 사용자에게 어울리는 노래를 추천
- 보컬 트레이닝보다 **시간적, 금전적으로 효율적인 효과**를 내는 서비스

<br><br>

## ✅ 주요 기능

- 사용자 음역대와 성향 분석과 그에 어울리는 **노래 추천**
- 추천한 노래 **PlayList** 관리
- 보컬 평가 및 피드백 **보고서 제공**

<br><br>

## 🖱️ 개발 환경

<img src="https://img.shields.io/badge/FrontEnd-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"><img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=black">

<img src="https://img.shields.io/badge/BackEnd-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"><img src="https://img.shields.io/badge/5.0.4-515151?style=for-the-badge">

<img src="https://img.shields.io/badge/Algorithm-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/3.10.11-3776AB?style=for-the-badge"><img src="https://img.shields.io/badge/Librosa-00BFFF?style=for-the-badge"><img src="https://img.shields.io/badge/spleeter-1D3557?style=for-the-badge"><img src="https://img.shields.io/badge/ffmpeg-007ACC?style=for-the-badge&logo=ffmpeg&logoColor=white"><img src="https://img.shields.io/badge/plotly-3F4C6B?style=for-the-badge&logo=plotly&logoColor=white"><img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">

<img src="https://img.shields.io/badge/Collaboration Tool-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white"><img src="https://img.shields.io/badge/Kakaotalk-FFCD00?style=for-the-badge&logo=Kakaotalk&logoColor=black"><img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white">

<img src="https://img.shields.io/badge/Design Tool-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white"><img src="https://img.shields.io/badge/clip studio-1DB6EA?style=for-the-badge">
<br><br>

## 📂 파일 구조

```bash
├── .github
│   ├── ISSUE_TEMPLATE
│   └── pull_request_template.md
│
├── MyV
│   ├── ..
│   ├── MyV
│   ├── login
│   ├── main
│   ├── media/maxminSrc
│   ├── modal
│   ├── myauth
│   ├── signup
│   ├── .gitignore
│   ├── db.sqlite3
│   └── manage.py
│
├── algorithm
│   ├── ..
│   ├── accuaracy_analyze.py
│   ├── audio_analysis.py
│   ├── get_recommendations.py
│   ├── text.txt
│   └── tmp_img.png
│
└── frontend
│   ├── ..
│   ├── howtouse
│   ├── login
│   ├── main
│   ├── mypage
│   ├── signup
│   ├── signup_Maxmin
│   ├── team
│   ├── vocalreport
│   └── wavetest
│
├── README.md
│
├── db.sqlite3

```

<br><br>

## ✨ 기능

### 1. 사용자 음역대와 성향 분석과 노래 추천

MyV를 이용하는 사람의 음악 성향 정보를 회원 가입에서 확보하고, 사용자가 업로드 하는 음원 파일로 Python 라이브러리 Librosa를 활용하여 사용자의 음역대를 분석한다. 분석된 정보를 이용하여, Spotify API를 기반으로 사용자의 성향에 맞는 음악을 3곡 추천한다. 곡 추천과 동시에 사용자 성향 및 음역대 정보를 제공함으로써, 사용자가 MyV 서비스를 이용하여 **자신에게 어울리는 노래의 성향**을 알 수 있게 한다.

#### 🧷 기능 이용 방법

- 회원가입 시, 사용자가 직접 자신의 **음악 성향 정보를 입력**한다.
  <img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/a0365e86-7fd7-4b95-b4e5-e009639a5f1e" width="180">

<br><br>

- **MyV**의 메인 화면에서 **음역대 파일을 제출**한다.
  <img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/0b53c6fe-c45a-4044-b9ca-23c336af5613" width="180">

<br><br>

- 음역대 정보와 사용자 성향 기반 **추천 노래를 확인**한다.
  <img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/21e2f46c-6cf9-419c-8ea6-499b377492c7" width="180">

<br><br>

### 2. 추천한 노래 PlayList 관리

사용자 성향을 기반으로 추천받은 노래 3곡 중 마음에 드는 곡을 선택해 사용자의 PlayList에 저장할 수 있다. 곡 미리듣기 서비스를 제공하고, 앨범 커버 클릭 시 Spotify의 곡 정보 페이지로 이동하여 **곡에 대한 정보를 충분히 제공함**으로써 사용자가 PlayList에 추가할 곡을 선택하는 것을 돕는다. <br>
 사용자 PlayList 페이지로 이동하면 사용자가 선택한 곡들이 저장되어 있다. 다른 곡을 추천받고 싶다면 "다시 추천 받기" 버튼을 클릭하여 곡 추천을 추가적으로 받을 수 있다. 마음에 들지 않는 곡은 "삭제" 버튼으로 삭제할 수 있도록 하여 **PlayList 관리의 편의성을 제공**한다.

#### 🧷 기능 이용 방법

- 추천 노래 확인 후, 3곡 중 1곡을 선택해 **나만의 PlayList**에 저장할 수 있다.

- 플레이리스트에 저장된 곡은 삭제가 가능하다.

- 곡을 새로 추천받을 수 있어, 사용자를 위한 **PlayList**를 만들 수 있다.

<img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/1e3295c4-e9af-4162-bb6c-bf36bcffd5fa" width="180">

<br><br>

### 3. 보컬 평가 및 피드백 보고서 제공

사용자가 노래를 불러 녹음한 파일을 업로드 하면 파이썬 라이브러리 Librosa를 기반으로 녹음 파일의 최고, 최저음, 가장 잘 부른 구간, 음정 정확도 등 사용자의 노래 녹음 파일을 분석한다. 이를 기반으로 사용자 보컬 피드백 보고서를 제공함으로써 **사용자가 자신의 노래 실력을 효율적으로 알 수 있게 한다.**

#### 🧷 기능 이용 방법

- 사용자의 노래 **녹음 파일을 업로드**한다.

<img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/9082af71-b427-4484-82a3-9470f2685f32" width="180">

<br><br>

- 제공된 보컬 분석 보고서로 **보컬 분석 결과를 확인**한다.

<img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/e4b1e110-af0b-489c-b2cd-df1299d54873" width="180">

<br><br><br><br>

## 🧑🏻‍🤝‍👩🏻 개발 인원

### 🧷 Frontend

|                                                         이성준                                                          |                                                                         이승연                                                                          |                                                         이시우                                                          |
| :---------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |
| ![성준](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/6d4220e8-a1a4-46bd-82c1-42a258f579fb) | ![KakaoTalk_20240531_154711714 (1) (1)](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/8f1396ff-37c6-4061-9244-fa12159cfb46) | ![시우](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/099cc563-b7c1-4d46-ab8d-32f17b9f055c) |
|                                           동국대학교 <br>컴퓨터공학과 21학번                                            |                                                            동국대학교<br> AI융합학부 22학번                                                             |                                           동국대학교<br> 컴퓨터공학과 22학번                                            |

<br>

### 🧷 Backend

|                                                         김지민                                                          |                                                         최예인                                                          |
| :---------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |
| ![지민](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/50e2f95c-20e9-4849-98ad-4f1a4665b40d) | ![예인](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/8496ba50-ab3a-4378-8903-41a6fd55e0a5) |
|                                           동국대학교<br> 컴퓨터공학과 22학번                                            |                                           동국대학교<br> 컴퓨터공학과 22학번                                            |

끝
