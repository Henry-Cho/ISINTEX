from django.urls import path
from .views import newPageView

urlpatterns = [
    path("new/", newPageView, name="new"),  
    ]