from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='profiles/',null=True, blank=True, default='profiles/222.jpg')
    bio = models.TextField(null=True, blank=True)
    contact_info = models.CharField(max_length=30 ,null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=30,null=True, blank=True)
    website_picture = models.ImageField(upload_to='uploads/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website_link = models.CharField(max_length=255,null=True, blank=True)
    design_score = models.IntegerField(default=1, null=True, blank=True)
    usability_score = models.IntegerField(default=1, null=True, blank=True)
    content_score = models.IntegerField(default=1, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title