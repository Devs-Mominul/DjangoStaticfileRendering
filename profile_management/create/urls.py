from django.urls import path
from create.views import *
urlpatterns = [
    path('', create, name='create'),
]  
