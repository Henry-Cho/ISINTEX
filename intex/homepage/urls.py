from django.urls import path
from .views import indexPageView, drugViewPage, drugDetailViewPage, searchDrug, analysisPageView, searchState

urlpatterns = [
    path("", indexPageView, name="index"),
    path('drug/', drugViewPage, name='drug'),
    path('drugdetail/<int:id>', drugDetailViewPage, name='drugdetail'),
    path('drugsearch/', searchDrug, name='drugsearch'),
    path('searchstate/<str:state>', searchState, name='searchState'),
    path('analysis/', analysisPageView, name='analysis')
    ]