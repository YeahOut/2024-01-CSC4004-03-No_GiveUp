from django.contrib import admin
from .models import UserMaxMinFile, UserMaxMinNote, PlaylistInfo

#관리자 페이지에서 UploadAnalyzeFile 모델 확인하기
class UserMaxMinFileAdmin(admin.ModelAdmin):
    pass

class UserMaxMinNoteAdmin(admin.ModelAdmin):
    list_display = ('user','min_note', 'max_note',)
    search_fields = ('user__username',)

class PlaylistInfoAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

admin.site.register(UserMaxMinFile,UserMaxMinFileAdmin)
admin.site.register(UserMaxMinNote,UserMaxMinNoteAdmin)
admin.site.register(PlaylistInfo,PlaylistInfoAdmin)