from django.db import models

# Create your models here.
class Profile (models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHERS', 'OTHERS'),
    )
    RELIGION = (
        ('ISLAM', 'ISLAM'),
        ('HINDU', 'HINDU'),
        ('OTHERS', 'OTHERS'),
    )
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='profile_img/', default='def.png')
    address = models.TextField()
    phone_number = models.TextField()
    gender = models.CharField(choices=GENDER, max_length=12)
    religion = models.CharField(choices=RELIGION, max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateTimeField()
    def __str__(self):
        return self.name
   
        

    
