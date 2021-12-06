from django.http import request
from django.shortcuts import render
from django.apps import apps
from django.db.models import Avg
from django.db.models import Q

Prescriber = apps.get_model('homepage', 'Prescriber')
Drugnpi = apps.get_model('homepage', 'Drugnpi')
Triple = apps.get_model('homepage', 'Triple')
Drug = apps.get_model('homepage', 'Drug')

# Create your views here.
def newPageView(request) :


    return render(request, 'prespage/new.html')

def newPresCreate(req):
    if req.method == "POST":
        newPres = Prescriber()
        newPres1 = Drugnpi()
        newPres2 = Triple()


        newPres.fname = req.POST.get("fname")
        newPres.lname = req.POST.get("lname")
        newPres.gender = req.POST.get("gender")
        newPres.state = req.POST.get("state")
        newPres.credentials = req.POST.get("credentials")
        newPres.specialty = req.POST.get("specialty")
        newPres.isopioidprescriber = req.POST.get("isopioidprescriber")
        newPres.totalprescriptions = 0
        newPres.save()

        newPres2.id = newPres.id
        newPres2.prescriberid = newPres.id
        newPres2.drugname = "abilify"
        newPres2.qty = 0
        newPres2.save()

        newPres1.id = newPres.id
        newPres1.abilify = 0
        newPres1.acetaminophencodeine = 0
        newPres1.acyclovir = 0
        newPres1.advairdiskus = 0
        newPres1.aggrenox = 0
        newPres1.alendronatesodium = 0
        newPres1.allopurinol = 0
        newPres1.alprazolam = 0
        newPres1.amiodaronehcl = 0
        newPres1.amitriptylinehcl = 0
        newPres1.amlodipinebesylate = 0
        newPres1.amlodipinebesylatebenazepril = 0
        newPres1.amoxicillin = 0
        newPres1.amoxtrpotassiumclavulanate = 0
        newPres1.amphetaminesaltcombo = 0
        newPres1.atenolol = 0
        newPres1.atorvastatincalcium = 0
        newPres1.avodart = 0
        newPres1.azithromycin = 0
        newPres1.baclofen = 0
        newPres1.bdultrafinepenneedle = 0
        newPres1.benazeprilhcl = 0
        newPres1.benicar = 0
        newPres1.benicarhct = 0
        newPres1.benztropinemesylate = 0
        newPres1.bisoprololhydrochlorothiazide = 0
        newPres1.brimonidinetartrate = 0
        newPres1.bumetanide = 0
        newPres1.bupropionhclsr = 0
        newPres1.bupropionxl = 0
        newPres1.buspironehcl = 0
        newPres1.bystolic = 0
        newPres1.carbamazepine = 0
        newPres1.carbidopalevodopa = 0
        newPres1.carisoprodol = 0
        newPres1.cartiaxt = 0
        newPres1.carvedilol = 0
        newPres1.cefuroxime = 0
        newPres1.celebrex = 0
        newPres1.cephalexin = 0
        newPres1.chlorhexidinegluconate = 0
        newPres1.chlorthalidone = 0
        newPres1.cilostazol = 0
        newPres1.ciprofloxacinhcl = 0
        newPres1.citalopramhbr = 0
        newPres1.clindamycinhcl = 0
        newPres1.clobetasolpropionate = 0
        newPres1.clonazepam = 0
        newPres1.clonidinehcl = 0
        newPres1.clopidogrel = 0
        newPres1.clotrimazolebetamethasone = 0
        newPres1.colcrys = 0
        newPres1.combiventrespimat = 0
        newPres1.crestor = 0
        newPres1.cyclobenzaprinehcl = 0
        newPres1.dexilant = 0
        newPres1.diazepam = 0
        newPres1.diclofenacsodium = 0
        newPres1.dicyclominehcl = 0
        newPres1.digox = 0
        newPres1.digoxin = 0
        newPres1.diltiazem24hrcd = 0
        newPres1.diltiazem24hrer = 0
        newPres1.diltiazemer = 0
        newPres1.diltiazemhcl = 0
        newPres1.diovan = 0
        newPres1.diphenoxylateatropine = 0
        newPres1.divalproexsodium = 0
        newPres1.divalproexsodiumer = 0
        newPres1.donepezilhcl = 0
        newPres1.dorzolamidetimolol = 0
        newPres1.doxazosinmesylate = 0
        newPres1.doxepinhcl = 0
        newPres1.doxycyclinehyclate = 0
        newPres1.duloxetinehcl = 0
        newPres1.enalaprilmaleate = 0
        newPres1.escitalopramoxalate = 0
        newPres1.estradiol = 0
        newPres1.exelon = 0
        newPres1.famotidine = 0
        newPres1.felodipineer = 0
        newPres1.fenofibrate = 0
        newPres1.fentanyl = 0
        newPres1.finasteride = 0
        newPres1.floventhfa = 0
        newPres1.fluconazole = 0
        newPres1.fluoxetinehcl = 0
        newPres1.fluticasonepropionate = 0
        newPres1.furosemide = 0
        newPres1.gabapentin = 0
        newPres1.gemfibrozil = 0
        newPres1.glimepiride = 0
        newPres1.glipizide = 0
        newPres1.glipizideer = 0
        newPres1.glipizidexl = 0
        newPres1.glyburide = 0
        newPres1.haloperidol = 0
        newPres1.humalog = 0
        newPres1.hydralazinehcl = 0
        newPres1.hydrochlorothiazide = 0
        newPres1.hydrocodoneacetaminophen = 0
        newPres1.hydrocortisone = 0
        newPres1.hydromorphonehcl = 0
        newPres1.hydroxyzinehcl = 0
        newPres1.ibandronatesodium = 0
        newPres1.ibuprofen = 0
        newPres1.insulinsyringe = 0
        newPres1.ipratropiumbromide = 0
        newPres1.irbesartan = 0
        newPres1.isosorbidemononitrateer = 0
        newPres1.jantoven = 0
        newPres1.janumet = 0
        newPres1.januvia = 0
        newPres1.ketoconazole = 0
        newPres1.klorcon10 = 0
        newPres1.klorconm10 = 0
        newPres1.klorconm20 = 0
        newPres1.labetalolhcl = 0
        newPres1.lactulose = 0
        newPres1.lamotrigine = 0
        newPres1.lansoprazole = 0
        newPres1.lantus = 0
        newPres1.lantussolostar = 0
        newPres1.latanoprost = 0
        newPres1.levemir = 0
        newPres1.levemirflexpen = 0
        newPres1.levetiracetam = 0
        newPres1.levofloxacin = 0
        newPres1.levothyroxinesodium = 0
        newPres1.lidocaine = 0
        newPres1.lisinopril = 0
        newPres1.lisinoprilhydrochlorothiazide = 0
        newPres1.lithiumcarbonate = 0
        newPres1.lorazepam = 0
        newPres1.losartanhydrochlorothiazide = 0
        newPres1.losartanpotassium = 0
        newPres1.lovastatin = 0
        newPres1.lovaza = 0
        newPres1.lumigan = 0
        newPres1.lyrica = 0
        newPres1.meclizinehcl = 0
        newPres1.meloxicam = 0
        newPres1.metforminhcl = 0
        newPres1.metforminhcler = 0
        newPres1.methadonehcl = 0
        newPres1.methocarbamol = 0
        newPres1.methotrexate = 0
        newPres1.methylprednisolone = 0
        newPres1.metoclopramidehcl = 0
        newPres1.metolazone = 0
        newPres1.metoprololsuccinate = 0
        newPres1.metoprololtartrate = 0
        newPres1.metronidazole = 0
        newPres1.mirtazapine = 0
        newPres1.montelukastsodium = 0
        newPres1.morphinesulfate = 0
        newPres1.morphinesulfateer = 0
        newPres1.mupirocin = 0
        newPres1.nabumetone = 0
        newPres1.namenda = 0
        newPres1.namendaxr = 0
        newPres1.naproxen = 0
        newPres1.nasonex = 0
        newPres1.nexium = 0
        newPres1.niaciner = 0
        newPres1.nifedicalxl = 0
        newPres1.nifedipineer = 0
        newPres1.nitrofurantoinmonomacro = 0
        newPres1.nitrostat = 0
        newPres1.nortriptylinehcl = 0
        newPres1.novolog = 0
        newPres1.novologflexpen = 0
        newPres1.nystatin = 0
        newPres1.olanzapine = 0
        newPres1.omeprazole = 0
        newPres1.ondansetronhcl = 0
        newPres1.ondansetronodt = 0
        newPres1.onglyza = 0
        newPres1.oxcarbazepine = 0
        newPres1.oxybutyninchloride = 0
        newPres1.oxybutyninchlorideer = 0
        newPres1.oxycodoneacetaminophen = 0
        newPres1.oxycodonehcl = 0
        newPres1.oxycontin = 0
        newPres1.pantoprazolesodium = 0
        newPres1.paroxetinehcl = 0
        newPres1.phenobarbital = 0
        newPres1.phenytoinsodiumextended = 0
        newPres1.pioglitazonehcl = 0
        newPres1.polyethyleneglycol3350 = 0
        newPres1.potassiumchloride = 0
        newPres1.pradaxa = 0
        newPres1.pramipexoledihydrochloride = 0
        newPres1.pravastatinsodium = 0
        newPres1.prednisone = 0
        newPres1.premarin = 0
        newPres1.primidone = 0
        newPres1.proairhfa = 0
        newPres1.promethazinehcl = 0
        newPres1.propranololhcl = 0
        newPres1.propranololhcler = 0
        newPres1.quetiapinefumarate = 0
        newPres1.quinaprilhcl = 0
        newPres1.raloxifenehcl = 0
        newPres1.ramipril = 0
        newPres1.ranexa = 0
        newPres1.ranitidinehcl = 0
        newPres1.restasis = 0
        newPres1.risperidone = 0
        newPres1.ropinirolehcl = 0
        newPres1.seroquelxr = 0
        newPres1.sertralinehcl = 0
        newPres1.simvastatin = 0
        newPres1.sotalol = 0
        newPres1.spiriva = 0
        newPres1.spironolactone = 0
        newPres1.sucralfate = 0
        newPres1.sulfamethoxazoletrimethoprim = 0
        newPres1.sumatriptansuccinate = 0
        newPres1.symbicort = 0
        newPres1.synthroid = 0
        newPres1.tamsulosinhcl = 0
        newPres1.temazepam = 0
        newPres1.terazosinhcl = 0
        newPres1.timololmaleate = 0
        newPres1.tizanidinehcl = 0
        newPres1.tolterodinetartrateer = 0
        newPres1.topiramate = 0
        newPres1.toprolxl = 0
        newPres1.torsemide = 0
        newPres1.tramadolhcl = 0
        newPres1.travatanz = 0
        newPres1.trazodonehcl = 0
        newPres1.triamcinoloneacetonide = 0
        newPres1.triamterenehydrochlorothiazid = 0
        newPres1.valacyclovir = 0
        newPres1.valsartan = 0
        newPres1.valsartanhydrochlorothiazide = 0
        newPres1.venlafaxinehcl = 0
        newPres1.venlafaxinehcler = 0
        newPres1.ventolinhfa = 0
        newPres1.verapamiler = 0
        newPres1.vesicare = 0
        newPres1.voltaren = 0
        newPres1.vytorin = 0
        newPres1.warfarinsodium = 0
        newPres1.xarelto = 0
        newPres1.zetia = 0
        newPres1.ziprasidonehcl = 0
        newPres1.zolpidemtartrate = 0
        newPres1.save()


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
    
    prescriber = Drugnpi.objects.get(id = id)
    presCount = record.totalprescriptions

    newlist = prescriber.__dict__

    arr1 = []

    total_count = 0

    for key,val in newlist.items():
        if key == '_state' or key == 'id' :
            continue
        if val == False :
            continue

        ab = Triple.objects.filter(drugname = key)
        ac = ab.aggregate(Avg('qty'))

        drug = Drug.objects.all()

        drug_real = ''
        drug_id = ''

        for i in drug :
            if (i.drugname.lower().replace('.', '') == key) :
                drug_real = i.drugname
                drug_id = i.id
                break

        key_name = ''

        for a in ac.keys() :
            key_name = a

        value = ac[key_name]
        round_val = round(value, 2)
        
        arr1.append({"id": drug_id, "name": drug_real, "avg": round_val})

        total_count += val
    
    context = {
        'pres': record,
        'count': total_count,
        'test': arr1,
        "presCount": presCount
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
    if req.method == 'POST':
        presid = req.POST['presid']

        pres = Prescriber.objects.get(id=presid)
        count = req.POST['count']
        pres.totalprescriptions += int(count)
        pres.isopioidprescriber = bool(pres.isopioidprescriber)
        pres.save()


        return PresDetailViewPage(req, presid)
    else:
        return PresViewPage(req)
