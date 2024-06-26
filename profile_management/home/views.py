from django.shortcuts import render
from create.models import Profile

# Create your views here.
def home(request):
    prof=Profile.objects.all()
    return render(request,'home/home.html',locals())
