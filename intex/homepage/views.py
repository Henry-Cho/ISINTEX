from django.shortcuts import render
from django.apps import apps
from .models import Drug

# Drug = apps.get_model('homepage','Drug')

# Create your views here.
def indexPageView(request) :
    return render(request, 'homepage/index.html')

def drugViewPage(req) :
    data = Drug.objects.all()

    context = {
        'druglist': data,
    }
    return render(req, 'homepage/drug.html', context)

def drugDetailViewPage(req, id) :

    record = Drug.objects.get(id= id)

    context = {
        'drug': record
    }

    return render(req, 'homepage/drugdetail.html', context)

