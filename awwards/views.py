from django.shortcuts import render,redirect
from .forms import RegisterForm

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

def index(request):
    return render(request, 'index.html')