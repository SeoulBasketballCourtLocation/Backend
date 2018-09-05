from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
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


def profile(request):
    return render(request, 'members/profile.html')