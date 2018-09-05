from django.contrib.auth import login
from django.shortcuts import render

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
