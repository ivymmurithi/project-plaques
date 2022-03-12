from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.profile1= Profile(bio= 'just here to rate projects and get motivated',contact_info='test@gmail.com')
        self.profile1.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile1,Profile))

    def test_save_method(self):
        self.profile1.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile1.save_profile()
        self.profile1.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) -1)

class ProjectTestClass(TestCase):

    def setUp(self):
        self.project1= Project(title='Akan names Project',description='This shows your Akan Name according to Ghananian Culture',website_link='https://test.com',design_score=8,usability_score=10,content_score=10)
        self.project1.save_project()

    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Project))

    def test_save_method(self):
        self.project1.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project1.save_project()
        self.project1.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) -1)
