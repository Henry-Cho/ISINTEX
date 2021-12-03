from django.shortcuts import render
from django.apps import apps
from .models import Drug, Prescriber

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

    drugName = record.drugname.lower().replace('.', '')

    print(drugName)

    sQuery = f'SELECT id, fname, lname, {drugName} AS drugQty FROM pd_prescriber '

    if (drugName != '') :
        sQuery += f'ORDER BY drugQty DESC LIMIT 10;'
    
    prescriberList = Prescriber.objects.raw(sQuery)

    context = {
        'drug': record,
        'prescriber': prescriberList
    }

    return render(req, 'homepage/drugdetail.html', context)

def searchDrug(req):
    input = req.GET['search']
    input2 = req.GET.get('filter')

    tf = 'False'

    if input2 == 'on' :
        tf = 'True'


    druglist = Drug.objects.filter(drugname__icontains=input)
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

# def searchEmpPageView(request) :
#     sFirst = request.GET['first_name']
#     sLast = request.GET['last_name']
#     sGrade_Level = request.GET['grade_level']
#     sQuery = 'SELECT Student.id, first_name, last_name, description FROM Student, Grade_Level WHERE Student.class_level_id = Grade_Level.class_level'
#     if sFirst != '' :
#         sQuery += " AND first_name = '" + sFirst + "'"
#     if sLast != '' :
#         sQuery += " AND last_name = '" + sLast + "'"
#     if sGrade_Level != '' :
#         sQuery += " AND class_level_id = '" + sGrade_Level + "'"        
#     sQuery += ' ORDER BY first_name, last_name, description'
#     data = Student.objects.raw(sQuery)
#     lookup = Grade_Level.objects.all()
#     context = {
#         "our_students" : data,
#         "grades" : lookup,
#     }
#     return render(request, 'travelpages/displayStudents.html', context) 
