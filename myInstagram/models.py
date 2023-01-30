from django.db import models
from django.contrib.auth.models import User


GENDER=(
    ("M","Mail"),
    ("F","Femail"),
    ("O","Other"),
)
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField()
    contact=models.IntegerField()
    gender=models.CharField(max_length=10,choices=GENDER)
    image=models.ImageField(upload_to="photo/",null=True,blank=True)
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    post_by=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="photo/",null=True,blank=True)
    caption= models.TextField()
    date_of_creation=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post_by.username
    
    