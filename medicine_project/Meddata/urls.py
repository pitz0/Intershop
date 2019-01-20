from django.urls import path
from django.conf.urls import include, url
from .views import *


urlpatterns = [
    path('medicine', ListMedicineView.as_view(), name="medicine-all"),
    path('home', home,name = "home"),
    path('landing',landing,name = 'landing'),
    path('specmed',SpecMedView.as_view(),name = 'specmed'),
    path('getmed',getmed,name = 'getmed'),
    
    ] 