from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True)


class UploadMAXMIN(models.Model):
    max_file = models.FileField(upload_to='userVoice/')
    min_file = models.FileField(upload_to='userVoice/')

class MaxminNote(models.Model):
    max_note = models.CharField(max_length=5)
    min_note = models.CharField(max_length=5)
