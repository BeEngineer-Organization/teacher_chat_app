from django.contrib import admin

from .models import User, Talk, Reply

admin.site.register(User)
admin.site.register(Talk)
admin.site.register(Reply)
