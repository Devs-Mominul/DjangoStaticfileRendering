from django.shortcuts import render
from create.models import Profile

# Create your views here.
def delete(request,id):
    prof=Profile.objects.get(id=id)
    prof.delete()
    
