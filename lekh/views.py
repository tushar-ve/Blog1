
from .models import *
# Create your views here.
from django.shortcuts import render, redirect  ,HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
import requests



@login_required(login_url='/login')
def home(request):
    posts= Post.objects.all().order_by('post_id')
    
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    postsDataList= paginator.get_page(page_number)
    totalpage= postsDataList.paginator.num_pages
    cats = Category.objects.all()

    # if request.method == "GET":
    #     st = request.GET.get('blog/url')
    #     if st!=None:
    #         posts=Post.objects.filter(url_icontains=st)
    # 
    
 

    # print(posts)
    data={
        'posts':posts,
        'posts': postsDataList,
        'cats': cats,
        'lastpage': totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)],
    }
    return render(request, "home.html", data)

@login_required(login_url='/login')
def search(request):

  st=request.GET.get('title')

  posts=Post.objects.filter(title__icontains=st)

  data={

    'posts':posts

  }

  return render(request,'search.html',data)

@login_required(login_url='/login')
def post(request, url):
    post= Post.objects.get(url=url)
    cats = Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        commentt=request.POST.get('comment')
        if name != "" and email !="":
          en = Comment(name=name,email=email,comment=commentt,post=post)
          en.save()
          return redirect("/home")
        
        else: 
            messages.error(request, "E-mail & Username must required")
    comment = Comment.objects.filter(post=post)
    # print(comment)




    
    
   
    return render(request, "posts.html", {'post':post,'cats':cats, 'comments':comment})

@login_required(login_url='/login')
def category(request, url):
    cat = Category.objects.get(url=url)
    posts= Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat':cat,'posts': posts})



def login_page(request):
    
    
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # clientKey = request.POST['g-recaptcha-response']
        # secretKey ='6Ld1ai0mAAAAAG2WFSKVkFDHXnCYu14ZsQATNk8m'
        # CaptchaData ={
        #     'secret': secretKey,
        #     'response': clientKey
        # }
        # r = requests.post('https://www.google.com/recaptcha/api/siteverpfy', data=CaptchaData)
        # response = json.loads(r.text)
        # verify = response['success']
        # print('you data is saved', verify)
        
        user= authenticate(username=username,password=password)
        print(user)
        if User.objects.filter(username=username):
            if User.objects.filter(password=password):
                if username!=None:
                
                        login(request, user)
                        return redirect("/home")
               
            else:
                messages.error(request, "Please Enter a valid password")
        else:
           messages.error(request, "Please Enter a valid Username")
         

    return render(request, "auth/index.html")

def register(request):
    
    if request.method == "POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password=request.POST.get('password')

        user= User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect("/")
        
        user = User.objects.create(
            username=username,
            email=email,
            password=password,
        )

        
        user.save()
        user.get_all_permissions()

        # messages.success(request, 'Account created Successfully')

         
        return redirect("/login")
  
    # messages.error(request,'The given input is already taken')

    return render(request,"auth/signup.html")


@login_required(login_url='/login')

def logout(request):

  auth.logout(request)

  return redirect('/login')