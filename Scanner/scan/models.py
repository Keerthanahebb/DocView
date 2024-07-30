from django.db import models
from django.utils import timezone

import uuid


import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    blood_group = models.CharField(default=" ",max_length=100)  # Make the field non-nullable
    ph_no = models.IntegerField(null=True,blank=True) 

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.localtime())
    img_name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.img_name if self.img_name else "No Name"