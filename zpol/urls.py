from django.urls import path
from . import views

urlpatterns = [
    path('', views.zpol_list),  
]
