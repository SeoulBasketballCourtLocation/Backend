import json

import requests
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from config.settings.production import secrets
from members import backends
from members.backends import KakaoBackend
from members.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return render(request, 'members/signup-done.html')
    else:
        form = SignupForm()
    context = {
        'form':form,
    }
    return render(request, 'members/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('index')
        else:
            return redirect('login')

    else:
        return render(request, 'members/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/members/login/')
def profile(request):
    return render(request, 'members/profile.html')

def change_profile(request):
    if request.method == 'POST':
        print(request.POST)
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        gender = request.POST['gender']
        main_position = request.POST['main_position']
        introduce = request.POST['introduce']
        user = request.user
        user.phone_number = phone_number
        user.email = email
        user.gender = gender
        user.main_position = main_position
        user.introduce = introduce
        user.save()
        messages.success(request, '개인정보가 수정되었습니다.')
        return redirect('profile')
    return render(request, 'members/change_profile.html')

def kakao_oauth(request):
    code = request.GET.get('code')
    user = authenticate(request, code=code)
    if user is not None:
        login(request, user)
        return redirect('index')
    return redirect('login')


