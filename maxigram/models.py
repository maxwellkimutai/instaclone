from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile_images',blank = True)
    bio = models.TextField(max_length = 100)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    image_name = models.CharField(max_length = 30)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
