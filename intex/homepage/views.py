from django.shortcuts import render
from django.apps import apps
from .models import Drug, Prescriber
from django.db.models import Avg

Drugnpi = apps.get_model('homepage','Drugnpi')
Triple = apps.get_model('homepage','Triple')

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

    drugName = record.drugname.lower().replace('.', '')

    sQuery = f'SELECT id, fname, lname, credentials, {drugName} AS drugqty FROM pd_prescribers '

    if (drugName != '') :
        sQuery += f'ORDER BY drugqty DESC LIMIT 10;'
    
    prescriberList = Prescriber.objects.raw(sQuery)

    print(prescriberList)

    context = {
        'drug': record,
        'prescriber': prescriberList,
        'name': drugName
    }

    return render(req, 'homepage/drugdetail.html', context)

def searchDrug(req):
    input = req.GET['search']
    input2 = req.GET.get('filter')

    tf = 'False'

    if input2 == 'on' :
        tf = 'True'

    if input != '':
        druglist = Drug.objects.filter(drugname__icontains=input)
    else :
        druglist = Drug.objects.all()

    newlist = druglist.filter(isopioid = tf)

    count = 0
    for d in newlist :
        count += 1
    
    obj = {
        "count": count
    }

    context = {
        'drug': newlist,
        'count': obj
    }

    return render(req, 'homepage/drugsearch.html', context)

def analysisPageView(req):
    return render(req, 'homepage/analysis.html')

def searchState(req, state) :
    data = Prescriber.objects.filter(state=state)
    print(data)
    count = 0
    for d in data :
        count += 1
    
    obj = {
        "count": count
    }
    
    context = {
        'drug': data,
        'count': obj
    }
    return render(req, 'prespage/search.html', context)
