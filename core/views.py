from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile

# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html',)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if(password==password2):
            if(User.objects.filter(email=email).exists()):
                messages.info(request, "Email already used")
                return redirect('signup')
            
            elif(User.objects.filter(username=username).exists()):
                messages.info(request, "Username already used")
                return redirect('signup')

            else:
                user= User.objects.create_user(username= username, email= email, password= password)
                user.save()
            
                user_model= User.objects.get(username= username)
                new_profile= Profile(user= user_model, id_user= user_model.id)
                new_profile.save()
                return redirect('index')

        else:
            messages.info(request, "Password not matching")
            return redirect('signup')

    else:
        return render(request, 'signup.html')