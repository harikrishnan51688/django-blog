from django.db import models
from django.contrib.auth.models import User
import uuid
from django_resized import ResizedImageField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=400, null=True, blank=True)
    profile_image = ResizedImageField(size=[250, 250], blank=True, null=True, default='images/profile_img/default.jpg', upload_to='images/profile_img/')
    short_intro = models.CharField(max_length=600, null=True, blank=True)
    website_link = models.URLField(max_length=800, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    profession = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.username)




