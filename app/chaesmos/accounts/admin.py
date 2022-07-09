from django.contrib import admin
from .models import *


class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)
