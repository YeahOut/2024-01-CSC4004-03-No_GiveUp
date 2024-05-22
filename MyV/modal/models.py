from django.db import models
from signup.models import User #Signup에서 만든 유저 모델을 FK로 사용하기 위해서 import 해주기

class UploadAnalyzeFile(models.Model):
    # AWS/vocalReportSource 디렉토리 버킷에 파일 업로드 
    mySound_file = models.FileField(upload_to='vocalReportSource/')
    compareSound_file = models.FileField(upload_to='vocalReportSource/')
    # 업로드한 파일명 저장
    fMySound_name = models.CharField(max_length=255, default='default')
    fCompareSound_name = models.CharField(max_length=255, default='default')

#사용자 음역대 저장할 모델
class UserVocalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #signup으로 로그인한 유저의 보컬분석후 음역대 정보 저장하기
    max_note = models.CharField(max_length=50, default = "none")
    min_note = models.CharField(max_length=50, default = "none")