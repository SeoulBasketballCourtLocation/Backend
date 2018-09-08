from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('img_profile', 'username', 'password1', 'password2', 'email', 'phone_number', 'gender', 'main_position', 'second_position', 'introduce')