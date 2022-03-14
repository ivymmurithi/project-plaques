from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileForm,ProjectForm,VotingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .models import Profile,Project
from rest_framework import viewsets
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import permissions
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('/login/')
    else:
        register_form=RegisterForm()
    return render(request,'registration/register.html',{'form':register_form})

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
# Create Profile
def profiles(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user_id = request.session['_auth_user_id'])
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profiles/',{'profile_form':form})
        else:
            profile_form = ProfileForm()
    else: 
        current_user = request.user
        profile_object = Profile.objects.all().filter(user=current_user.id)
        project_object = Project.objects.all().filter(user=current_user.id)
        profile_form = ProfileForm()
        project_form = ProjectForm()
        vote_form = VotingForm()
    return render(request, 'profiles.html',{'profiles':profile_object,'profile_form':profile_form,'projects':project_object,'project_form':project_form,'vote_form':vote_form})

@login_required
# Update Profile
def uploadproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['user_id'] = request.session['_auth_user_id']
            image = form.save()
            image.user_id = request.session['_auth_user_id']
            image.save()
            return redirect('profiles/',{'project_form':form})
        else:
            form = ProjectForm()
    else:
        form = ProjectForm()
    return render(request,'profiles.html',{'project_form':form})

@login_required
def vote(request, project_id):
    if request.method == 'POST':
        project = Project.objects.get(pk=project_id)
        vote_form = VotingForm(request.POST, instance=project)
        if vote_form.is_valid():
            vote_form.save()
            return redirect('/profiles/',{'vote_form':vote_form})
        else:
            vote_form = VotingForm()
    else:
        vote_form = VotingForm()
    return render(request, 'profiles.html',{'vote_form':vote_form})

@login_required
def results(request):
    if request.method == 'POST':
        if 'profiles' in request.POST and request.POST['profiles']:
            searched_profile = request.POST['profiles']
            profile_objects = Profile.objects.filter(user__username__icontains=searched_profile)
            profile_ids = [profile.user.id for profile in profile_objects]
            projects_objects = Project.objects.filter(user_id__in=profile_ids)
            return render(request, 'search.html', {'searchedprofiles':profile_objects,'searchedprojects':projects_objects})
        else:
            messages.error(request, "User does not exist!")
    return render(request, 'search.html')

@login_required
def logout(request):
    django_logout(request)
    return redirect('login')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]