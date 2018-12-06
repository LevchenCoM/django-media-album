from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    user_creation_form = UserCreationForm()
    if request.method=='POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            username=user_creation_form.cleaned_data['username']
            password=user_creation_form.cleaned_data['password1']
            new_user=User.objects.create_user(username=username,password=password)
            login(request, authenticate(username=username,password=password))
            return redirect('/')
    return render(request, "account/register.html", {'form':user_creation_form})
