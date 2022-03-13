from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','contact_info']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['website_picture','title','description','website_link','design_score','usability_score','content_score']