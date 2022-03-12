from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='profiles/',null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    contact_info = models.CharField(max_length=30 ,null=False, blank=False)

class Project(models.Model):
    title = models.CharField(max_length=30,null=False, blank=False,)
    website_picture = models.ImageField(upload_to='uploads/',null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    website_link = models.CharField(max_length=255,null=False, blank=False)