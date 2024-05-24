from django.contrib import admin
from .models import UserMaxMinFile, UserMaxMinNote

#관리자 페이지에서 UploadAnalyzeFile 모델 확인하기
class UserMaxMinFileAdmin(admin.ModelAdmin):
    pass

class UserMaxMinNoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserMaxMinFile,UserMaxMinFileAdmin)
admin.site.register(UserMaxMinNote,UserMaxMinNoteAdmin)
