from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['birthdate', 'avatar']

class ProfileAdmin(UserAdmin):
    Inlines = [ProfileInline]

User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)