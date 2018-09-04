from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    CHOICE_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함')
    )
    CHOICE_POSITION = (
        ('PG', '포인트 가드'),
        ('SG', '슈팅 가드'),
        ('SF', '스몰 포워드'),
        ('PF', '파워 포워드'),
        ('C', '센터'),
    )
    img_profile = models.ImageField(upload_to='user', blank=True)
    introduce = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    main_position = models.CharField(max_length=25, choices=CHOICE_POSITION)
    second_position = models.CharField(max_length=25, choices=CHOICE_POSITION)

    def __str__(self):
        return self.username
