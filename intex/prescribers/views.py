from django.shortcuts import render
from django.apps import apps

Prescriber = apps.get_model('homepage', 'Prescriber')

# Create your views here.
def newPageView(request) :
    data = Prescriber.objects.all()

    idx = 0
    ddd = ''
    for d in data :
        if idx > 0 :
            break
        ddd = d
        idx = idx + 1

    context = {
        'pres': ddd
    }

    return render(request, 'prespage/new.html', context)