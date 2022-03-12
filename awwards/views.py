from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    return render(request, 'profiles.html')

@login_required
def logout(request):
    logout(request)
    return redirect('login')