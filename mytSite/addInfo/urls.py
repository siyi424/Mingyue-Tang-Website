from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),  # http://127.0.0.1:8000/addInfo/register 
    path('searchName', searchName), # http://127.0.0.1:8000/addInfo/searchName
]


