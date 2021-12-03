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

def PresViewPage(req) :
    data = Prescriber.objects.all()

    context = {
        'preslist': data,
    }
    return render(req, 'prespage/prescribers.html', context)

def PresDetailViewPage(req, id) :
    record = Prescriber.objects.get(id= id)
    context = {
        'pres': record
    }
    return render(req, 'prespage/presdetail.html', context)