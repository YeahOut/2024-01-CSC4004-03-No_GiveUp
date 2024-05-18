from django.db import models

class UploadAnalyzeFile(models.Model):
    # 기존의 한 사용자로부터 인스턴스가 두 개씩 생기는 문제 방지 by setting user id as FK 
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # AWS/vocalReportSource 디렉토리 버킷에 파일 업로드 
    mySound_file = models.FileField(upload_to='vocalReportSource/')
    compareSound_file = models.FileField(upload_to='vocalReportSource/')
    # 업로드한 파일명 저장
    fMySound_name = models.CharField(max_length=255, default='default')
    fCompareSound_name = models.CharField(max_length=255, default='default')