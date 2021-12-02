from django.shortcuts import render

# Create your views here.
def govPageView(request) :
    return render(request, 'govpage/gov.html')