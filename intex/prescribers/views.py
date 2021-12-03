from django.http import request
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

def newPresCreate(req):
    if req.method == "POST":
        newPres = Prescriber()

        newPres.fname = req.POST.get("fname")
        newPres.lname = req.POST.get("lname")
        newPres.gender = req.POST.get("gender")
        newPres.state = req.POST.get("state")
        newPres.credentials = req.POST.get("credentials")
        newPres.specialty = req.POST.get("specialty")
        newPres.isopioidprescriber = req.POST.get("isopioidprescriber")
        newPres.totalprescriptions = req.POST.get("totalprescriptions")
        newPres.save()
        return PresDetailViewPage(request)
    else:
        data = Prescriber.objects.all()
        context = {
            "preslist" : data
            }
        
        return render(request, 'prespage/prescribers.html', context)

def updatePres(request, presid):
    data = Prescriber.objects.get(id = presid)

    context = {
        "pres": data
    }
    return render(request, 'prespage/editPres.html', context)


def updatePresSubmit(request):
    if request.method == 'POST':
        presid = request.POST['presid']

        pres = Prescriber.objects.get(id=presid)

        pres.fname = request.POST['fname']
        pres.lname = request.POST['lname']
        pres.gender = request.POST['gender']
        pres.state = request.POST['state']
        pres.credentials = request.POST['credentials']
        pres.specialty = request.POST['specialty']
        pres.isopioidprescriber = request.POST['isopioidprescriber']

        pres.save()
        return PresDetailViewPage(request, presid)
    else:
        data = Prescriber.objects.all()
        context = {
            "preslist" : data
            }
        
        return render(request, 'prespage/prescribers.html', context)


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