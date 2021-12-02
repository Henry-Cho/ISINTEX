from django.shortcuts import render

# Create your views here.
def newPageView(request) :
    return render(request, 'prespage/new.html')