from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Follow, MyUser


class MyUserAdmin(UserAdmin):
    list_filter = ('email', 'username')


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Follow)
