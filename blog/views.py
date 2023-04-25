from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

@login_required(login_url='/login/')
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def landing(request):
    return render(request, 'blog/landing.html')

def your_info(request):
    return render(request, 'blog/your_info.html')


def sign_up(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            return render(request, 'blog/home.html')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})