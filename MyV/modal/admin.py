from django.contrib import admin
from .models import UploadAnalyzeFile, UserVocalInfo

#관리자 페이지에서 UploadAnalyzeFile 모델 확인하기
class UploadAnalyzeFileAdmin(admin.ModelAdmin):
    pass

class UserVocalInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(UploadAnalyzeFile,UploadAnalyzeFileAdmin)
admin.site.register(UserVocalInfo,UserVocalInfoAdmin)