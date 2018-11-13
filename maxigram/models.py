from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile_images',blank = True)
    bio = models.TextField(max_length = 100,blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    followers = models.ManyToManyField(User,blank=True,related_name='followers')

    def save_profile(self):
        self.save()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search(cls,username):
        user = User.objects.get(username = username)
        return user

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True,related_name='post_likes')
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def get_images(cls):
        images = cls.objects.all().order_by('-pub_date')
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,caption):
        self.image_caption = caption
        self.save()

class Comment(models.Model):
    comment = models.CharField(max_length = 1000)
    image = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
