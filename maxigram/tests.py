from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(user = self.user)
        self.profile.save()
        self.image = Image(id=1,image = 'path/to/image',image_name='test',image_caption='test caption',user=self.user,profile=self.profile)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    #Testing Save method
    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    #Testing Update Method
    def test_update_caption(self):
        self.image.save_image()
        self.image = Image.objects.get(pk = 1)
        self.image.update_caption('updated caption')
        self.updated_image = Image.objects.get(id = 1)
        self.assertEqual(self.updated_image.image_caption,"updated caption")

    #Testing Delete Method
    def test_delete_image(self):
        self.image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(id=1,profile_photo='path/to/photo',user = self.user,bio='test bio')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    #Testing save method
    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    #Testing updtae method
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile = Profile.objects.get(pk = 1)
        self.profile.update_bio('updated bio')
        self.updated_profile = Profile.objects.get(pk = 1)
        self.assertEqual(self.updated_profile.bio,"updated bio")

    #Testing Delete Method
    def test_delete_image(self):
        self.profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)
