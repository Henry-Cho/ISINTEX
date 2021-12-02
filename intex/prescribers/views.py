from django.shortcuts import render

# Create your views here.
def aboutPageView(request) :
    return render(request, 'prespage/about.html')