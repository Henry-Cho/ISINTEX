from django.urls import path
from .views import newPageView, PresViewPage, PresDetailViewPage

urlpatterns = [
    path("new/", newPageView, name="new"),
    path("pres/", PresViewPage, name ='pres'),
    path('prescribers/<int:id>', PresDetailViewPage, name='presdetail'),
    ]