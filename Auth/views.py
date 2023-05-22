from django.shortcuts import render, redirect  
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def login_page(request):
    
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect("/login")
        
        user= authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login')
        
        else:
            login(request, user)
            return redirect('/home/')

    return render(request, "auth/index.html")

def register(request):
    
    if request.method == "POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password=request.POST.get('password')

        user= User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect("auth/signup.html")
        
        user = User.objects.create(
            username=username,
            email=email,
            password=password,
        )

        
        user.save()

        # messages.success(request, 'Account created Successfully')

         
        return redirect("/login")

    return render(request,"auth/signup.html")