from django.db.models.aggregates import Count
from django.http import request
from django.shortcuts import render
from django.apps import apps
from django.db.models import Avg
from django.db.models import Q

Prescriber = apps.get_model('homepage', 'Prescriber')
Drugnpi = apps.get_model('homepage', 'Drugnpi')
Triple = apps.get_model('homepage', 'Triple')

# Create your views here.
def newPageView(request) :


    return render(request, 'prespage/new.html')

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

        return PresViewPage(req)
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
    
    # length of total record
    record_len = Prescriber.objects.count()
    print(record_len)

    # length of record without this particular prescriber
    without_this= Prescriber.objects.filter(~Q(id=id)).count()

    print(without_this)

    # whole record
    whole_record = Drugnpi.objects.all()
    whole_list = whole_record.__dict__
    
    prescriber = Drugnpi.objects.get(id = id)

    newlist = prescriber.__dict__

    arr = []

    arr1 = []

    total_count = 0
        
    deduct_zero = 0

    for key,val in newlist.items():
        if val != False :
            if key == '_state' or key == 'id' :
                continue
            arr.append(key)
            # sQuery = f'SELECT id, ((sum({key}) - {val}) / ({record_len} - 1)) AS avgdrug FROM pd_prescriber group by id having id <> {id};'
            # ss = Prescriber.objects.raw(sQuery)
            ss = Prescriber.objects.all()
            sa = ss.aggregate(Avg(key))

            a = Triple.objects.filter(~Q(prescriberid = id, qty = 0))
            ab = a.filter(drugname = key)
            ac = ab.aggregate(Avg('qty'))

            key_name = ''

            for a in ac.keys() :
                key_name = a

            value = ac[key_name]
            round_val = round(value, 2)
            
            arr1.append({"name": key, "avg": round_val})
    
            total_count += val
    
    context = {
        'pres': record,
        'drug': arr,
        'count': total_count,
        'test': arr1
    }
    return render(req, 'prespage/presdetail.html', context)

def pressearch(req):
    input = req.GET['search']
    input2 = req.GET['search1']
    input3 = req.GET['search2']
    input4 = req.GET['search3']
    input5 = req.GET['search4']
    input6 = req.GET['search5']

    if input != '':
        preslist = Prescriber.objects.filter(fname__icontains=input)
    else :
        preslist = Prescriber.objects.all()

    newlist = preslist.filter(lname__icontains=input2)

    newlist1 = newlist.filter(gender__icontains=input3)
    newlist2 = newlist1.filter(credentials__icontains=input4)
    newlist3 = newlist2.filter(state__icontains=input5)
    newlist4 = newlist3.filter(specialty__icontains=input6)

    count = 0
    for d in newlist4 :
        count += 1
    
    obj = {
        "count": count
    }

    context = {
        'drug': newlist4,
        'count': obj
    }

    return render(req, 'prespage/search.html', context)


def delete(req, presid):
    data = Prescriber.objects.get(id = presid)

    data.delete()

    return PresViewPage(req)

def updateCount(req, presid):
    data = Prescriber.objects.get(id = presid)

    context = {
        "pres": data
    }
    return render(req, 'prespage/updatecount.html', context)

def updateCountNum(req):
    # if req.method == 'POST':
    #     presid = req.POST['presid']
    #     drugName = req.POST['drug']

    #     pres = Prescriber.objects.get(id=presid)

    #     print(pres)
    #     pres.drugName += req.POST['count']


    #     pres.save()
    #     return PresDetailViewPage(req, presid)
    # else:
        return PresViewPage(req)
