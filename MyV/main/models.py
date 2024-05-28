from django.db import models
from signup.models import User

#사용자 음역대 파일 이름 저장하는 모델
class UserMaxMinFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    min_file = models.FileField(upload_to='userVoice/')
    max_file = models.FileField(upload_to='userVoice/')
    min_file_name = models.CharField(max_length=255, default="none")
    max_file_name = models.CharField(max_length=255, default="none")

class UserMaxMinNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #signup으로 로그인한 유저의 보컬분석후 음역대 정보 저장하기
    max_note = models.CharField(max_length=50, default = "none")
    min_note = models.CharField(max_length=50, default = "none")

class PlaylistInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img1 = models.CharField(max_length=255, default="none")
    img2 = models.CharField(max_length=255, default="none")
    img3 = models.CharField(max_length=255, default="none")
    artist1 = models.CharField(max_length=255, default="none")
    artist2 = models.CharField(max_length=255, default="none")
    artist3 = models.CharField(max_length=255 ,default="none")
    title1 = models.CharField(max_length=255, default="none")
    title2 = models.CharField(max_length=255, default="none")
    title3 = models.CharField(max_length=255, default="none")
    songurl1 = models.CharField(max_length=255, default="none")
    songurl2 = models.CharField(max_length=255, default="none")
    songurl3 = models.CharField(max_length=255, default="none")
