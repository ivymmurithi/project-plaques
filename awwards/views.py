from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileForm
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
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # import pdb; pdb.set_trace()
            form.save()
            return redirect('/profiles/',{'profile_form':form})
        else:
            profile_form = ProfileForm()
    else: 
        current_user = request.user
        profile_object = Profile.objects.all().filter(user=current_user.id)
        profile_form = ProfileForm()
    return render(request, 'profiles.html',{'profiles':profile_object,'profile_form':profile_form})

@login_required
def logout(request):
    logout(request)
    return redirect('login')