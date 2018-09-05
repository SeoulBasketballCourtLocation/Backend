from django.contrib import admin
from django.contrib.auth import get_user_model

from config.settings.base import AUTH_USER_MODEL

User = get_user_model()
admin.site.register(User)