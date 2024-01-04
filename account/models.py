from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
        ('Regular Users', 'Regular Users'),
    )
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, blank=True, null=True, max_length=50)
    profile_picture = models.ImageField(upload_to='user/profile_picture/', blank=True, null=True)
    
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.first_name+' '+self.last_name