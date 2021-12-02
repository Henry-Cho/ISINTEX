from django.urls import path
from .views import govPageView

urlpatterns = [
    path("", govPageView, name="gov"),  
    ]