from django.contrib import admin

from .models import Follow, MyUser

admin.site.register(MyUser)
admin.site.register(Follow)
