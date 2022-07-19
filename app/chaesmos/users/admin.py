from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount, UsersAdmin)
admin.site.register(UserSession, UsersAdmin)
