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
-  LIBROSA 라이브러리 기반 **사용자** 최고음, 최저음, 음역대, **성향을 기반**으로 정보를 분석
-  사용자의 목소리를 분석하여 사용자에게 어울리는 노래를 추천
-  보컬 트레이닝보다 **시간적, 금전적으로 효율적인 효과**를 내는 서비스


<br><br>

## ✅ 주요 기능
- 사용자 음역대와 성향 분석과 그에 어울리는 **노래 추천**
- 추천한 노래 **PlayList** 관리
- 보컬 평가 및 피드백 **보고서 제공**

<br><br>

## 🖱️ 개발 환경
<img src="https://img.shields.io/badge/FrontEnd-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"><img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=black">

<img src="https://img.shields.io/badge/BackEnd-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"><img src="https://img.shields.io/badge/5.0.4-515151?style=for-the-badge">

<img src="https://img.shields.io/badge/Algorithm-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/3.10.11-3776AB?style=for-the-badge"><img src="https://img.shields.io/badge/Librosa-00BFFF?style=for-the-badge">

<img src="https://img.shields.io/badge/Collaboration Tool-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white"><img src="https://img.shields.io/badge/Kakaotalk-FFCD00?style=for-the-badge&logo=Kakaotalk&logoColor=black"><img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white">

<img src="https://img.shields.io/badge/Design Tool-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white">

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

- 추천 노래 확인 후, 3곡 중 1곡을 선택해 **나만의 PlayList**에 저장할 수 있다.

- 플레이리스트에 저장된 곡은 삭제가 가능하다.

- 곡을 새로 추천받을 수 있어, 사용자를 위한 **PlayList**를 만들 수 있다.

<img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/1e3295c4-e9af-4162-bb6c-bf36bcffd5fa" width="180">

<br><br>

### 3. 보컬 평가 및 피드백 보고서 제공

- 사용자의 노래 **녹음 파일을 업로드**한다. 

<img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/9082af71-b427-4484-82a3-9470f2685f32" width="180">

<br><br>

- 제공된 보컬 분석 보고서로 **보컬 분석 결과를 확인**한다.

<img src="https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/e4b1e110-af0b-489c-b2cd-df1299d54873" width="180">


<br><br><br><br>


## 🧑🏻‍🤝‍👩🏻 개발 인원 

### 🧷 Frontend

|이성준|이승연|이시우|
|:-----:|:-----:|:-----:|
|![성준](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/6d4220e8-a1a4-46bd-82c1-42a258f579fb)|![승연](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/0cca97c1-36e9-417b-9c21-7b223d7e6c36)|![시우](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/099cc563-b7c1-4d46-ab8d-32f17b9f055c)|
|동국대학교 <br>컴퓨터공학과 21학번|동국대학교<br> AI융합학부 22학번|동국대학교<br> 컴퓨터공학과 22학번|

<br>

### 🧷 Backend

|김지민|최예인|
|:-----:|:-----:|
|![지민](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/50e2f95c-20e9-4849-98ad-4f1a4665b40d)|![예인](https://github.com/CSID-DGU/2024-01-CSC4004-03-No_GiveUp/assets/137425231/8496ba50-ab3a-4378-8903-41a6fd55e0a5)|
|동국대학교<br> 컴퓨터공학과 22학번|동국대학교<br> 컴퓨터공학과 22학번|
