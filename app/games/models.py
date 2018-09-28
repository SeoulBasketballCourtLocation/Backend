from datetime import timezone

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from courts.models import Court

User = get_user_model()

class Game(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    curr_player = models.IntegerField(default=1)
    need_player = models.IntegerField(default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


