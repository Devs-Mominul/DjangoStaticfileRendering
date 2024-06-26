from django.shortcuts import render
from create.models import Profile

# Create your views here.
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('file')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        date_of_birth = request.POST.get('date_of_birth')
        print(name,email,image)
        try:
            if image:
                  
                   prof =Profile.objects.create(name=name, email=email, image=image, address=address, phone_number=phone_number, gender=gender, religion=religion, date_of_birth=date_of_birth )
                   prof.save()
                   
            else:
                 prof=Profile.objects.create(name=name, email=email,  address=address, phone_number=phone_number, gender=gender, religion=religion, date_of_birth=date_of_birth )
                 prof.save()
        except:
              pass
                
     
    return render(request, 'create/create.html')

