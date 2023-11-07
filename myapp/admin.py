from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','email', 'phone_number', 'password', 'otp_code', 'email_verified', 'is_admin', 'is_superadmin')  
    list_display_links = ('id', 'username','email', 'phone_number', 'password', 'otp_code', 'email_verified', 'is_admin', 'is_superadmin')  

admin.site.register(User, UserAdmin)

class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('id', ' user_id','first_name')  
    list_display_links = ('id', ' user_id','first_name')  

# admin.site.register(User, ReceptionistAdmin)