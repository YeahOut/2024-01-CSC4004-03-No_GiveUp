from django.db import models

class UploadAnalyzeFile(models.Model):
    mySound_file = models.FileField(upload_to='vocalReportSource/')
    compareSound_file = models.FileField(upload_to='vocalReportSource/')
    fMySound_name = models.CharField(max_length=255, default='default')
    fCompareSound_name = models.CharField(max_length=255, default='default')