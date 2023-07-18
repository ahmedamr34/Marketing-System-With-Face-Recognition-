from django.contrib.auth.models import AbstractUser
from django.db import models



class UserReg(AbstractUser):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)




    def __str__(self):
        return self.username
    



