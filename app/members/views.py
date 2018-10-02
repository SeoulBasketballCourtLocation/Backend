from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from members.forms import SignupForm, UpdateProfile


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return render(request, 'members/signup-done.html')
    else:
        form = SignupForm()
    context = {
        'form': form,
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
        form = UpdateProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfile(instance=request.user)
        context = {
            'form':form,
        }
        return render(request, 'members/change_profile.html', context)


def kakao_oauth(request):
    code = request.GET.get('code')
    user = authenticate(request, code=code)
    if user is not None:
        login(request, user)
        return redirect('index')
    return redirect('login')
