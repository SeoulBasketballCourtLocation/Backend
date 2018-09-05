from django.shortcuts import render

def signup(request):
    # if request.method == 'POST':
    return render(request, 'members/signup.html')
