from django.shortcuts import render, redirect
from .models import sty
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout  
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password1)
        
        
        return redirect('login')  # Redirect to dashboard or some other page after successful registration
    
    return render(request, 'register.html') 


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        # Authenticate user
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            # Login the user
            auth_login(request, user) 
            return redirect('home')  # Redirect to dashboard or some other page on successful login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
            

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


# Create your views here.
@login_required
def insert(request):
    if request.method == 'POST':
        eid=request.POST['eid']
        name=request.POST['name']
        dob=request.POST['dob']
        contact=request.POST['contact']
        photo=request.FILES.get('photo')
        k=sty(eid=eid,name=name,dob=dob,contact=contact,photo=photo)
        k.save()
        return redirect('cards')
    return render(request, 'create.html',)

@login_required
def cards(request):
    if request.method == 'GET':
        l=sty.objects.all()
    return render(request, 'cards.html', {'l':l})

    



