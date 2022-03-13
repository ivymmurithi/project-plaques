from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileForm,ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile,Project

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        else:
            return redirect('/')
    else:
        register_form=RegisterForm()
    return render(request,'registration/register.html',{'form':register_form})

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def profiles(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user_id = request.session['_auth_user_id'])
        # project = Project.objects.get(user_id = request.session['_auth_user_id'])
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        # project_form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            # import pdb; pdb.set_trace()
            form.save()
            # project_form.save()
            return redirect('/profiles/',{'profile_form':form})
        else:
            profile_form = ProfileForm()
            # project_form = ProjectForm()
    else: 
        current_user = request.user
        profile_object = Profile.objects.all().filter(user=current_user.id)
        project_object = Project.objects.all().filter(user=current_user.id)
        profile_form = ProfileForm()
        project_form = ProjectForm()
    return render(request, 'profiles.html',{'profiles':profile_object,'profile_form':profile_form,'projects':project_object,'project_form':project_form})

@login_required
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
def logout(request):
    logout(request)
    return redirect('login')