from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#@admin.register(User)
'''class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'user_ID', 'user_mood', 'user_energy', 'user_tempo', 'is_admin', 'is_staff', 'is_superadmin', 'is_active')
    search_fields = ('email', 'username', 'user_ID')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()'''
    
    
admin.site.register(User, UserAdmin)

