from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_name', 'ID', 'user_mood', 'user_energy', 'user_tempo', 'is_admin', 'is_staff', 'is_superadmin', 'is_active')
    search_fields = ('email', 'user_name', 'ID')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
