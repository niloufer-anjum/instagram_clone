from django.shortcuts import render
from .forms import UserForm, BioForm
from django.conf import settings

# Create your views here.
def login(request):
    pass

def logout(request):
    pass

def register(request):
    user_form = UserForm()
    bio_form = BioForm()

    context = {"user_form": user_form, "bio_form": bio_form}
    return render(request, "users/register.html", context)