from django.shortcuts import render

from courts.models import Court


def courts_list(request):
    courts = Court.objects.all()
    context = {
        'courts':courts,
    }
    return render(request, 'courts/courts_list.html', context)
