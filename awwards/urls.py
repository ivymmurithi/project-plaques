from django.db import router
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile',views.ProfileViewSet, basename='profile')
router.register(r'project', views.ProjectViewSet, basename='project')

urlpatterns = [
    path('api/',include(router.urls)),
    path('register/',views.register,name='register'),
    path('', include('django.contrib.auth.urls')),
    path('',views.index,name='index'),
    path('profiles/',views.profiles,name='profiles'),
    path('logout',views.logout,name='logout'),
    path('uploadproject',views.uploadproject,name='uploadproject'),
    path('vote/<int:project_id>/',views.vote,name='vote'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)