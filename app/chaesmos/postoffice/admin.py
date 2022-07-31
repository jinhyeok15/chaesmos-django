from django.contrib import admin
from .models import *


class PostofficeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Letter, PostofficeAdmin)
admin.site.register(Solution, PostofficeAdmin)
