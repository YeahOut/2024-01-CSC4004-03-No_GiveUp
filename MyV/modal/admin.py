from django.contrib import admin
from .models import UploadAnalyzeFile

#관리자 페이지에서 UploadAnalyzeFile 모델 확인하기
class UploadAnalyzeFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UploadAnalyzeFile,UploadAnalyzeFileAdmin)