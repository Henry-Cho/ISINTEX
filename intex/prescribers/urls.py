from django.urls import path
from .views import newPageView, PresViewPage, PresDetailViewPage, newPresCreate, updatePres, updatePresSubmit, pressearch

urlpatterns = [
    path("new/", newPageView, name="new"),
    path("pres/", PresViewPage, name ='pres'),
    path('<int:id>', PresDetailViewPage, name='presdetail'),
    path('createNew/', newPresCreate, name='newPres'),
    path('update/<int:presid>/', updatePres, name="update"),
    path("updatePres/", updatePresSubmit, name='updatePres'),
    path("pressearch/", pressearch, name="pressearch")
    ]