from django.db import models
from django.contrib.auth.models import User

#create a "Profile" Model
class Profile(models.Model):
    #create a relationship between Users and Profiles
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=120)
    pict = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return(f'{self.user.username} Profile')

