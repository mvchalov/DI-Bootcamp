from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image_file = models.ImageField(upload_to='media/')
    image_title = models.CharField(max_length=50, null=True, blank=True)
    image_description = models.TextField(null=True, blank=True)
    image_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.image_title} by {self.image_owner.get_username()}'


class Profile(models.Model):
    profile_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_collection = models.IntegerField()

    def __str__(self):
        return f'{self.profile_owner.get_username()} with {self.profile_collection} image/s'
