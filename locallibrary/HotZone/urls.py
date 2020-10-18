from django.contrib import admin
from django.urls import include,path 
from HotZone import views
from django.views.generic import RedirectView
urlpatterns = [
    path('', views.index, name='index'),
    path('Home',views.index ,name='home'),
    path('Virus/',views.VirusListView.as_view(),name='virus'),
    path('Patient/',views.PatientListView.as_view(),name='patient'),
    path('Case/',views.CaseListView.as_view(),name='case'),
    path('Location/',views.LocationListView.as_view(),name='location'),
    # path('Search/'), #在search当中implement使用外部API进行地址的添加
]