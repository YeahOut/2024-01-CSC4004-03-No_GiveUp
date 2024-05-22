from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        error_messages={'unique': "이미 사용중인 닉네임입니다!"},
        validators=[validate_no_special_characters],
        )


class UploadMAXMIN(models.Model):
    max_file = models.FileField(upload_to='userVoice/')
    min_file = models.FileField(upload_to='userVoice/')

class MaxminNote(models.Model):
    max_note = models.CharField(max_length=5)
    min_note = models.CharField(max_length=5)
