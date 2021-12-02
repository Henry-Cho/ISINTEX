from django.urls import path
from .views import indexPageView, drugViewPage, drugDetailViewPage

urlpatterns = [
    path("", indexPageView, name="index"),
    path('drug/', drugViewPage, name='drug'),
    path('drugdetail/<int:id>', drugDetailViewPage, name='drugdetail'),
    ]