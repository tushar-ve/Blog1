from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
from django.core.paginator import Paginator

def home(request):
    posts= Post.objects.all()
    
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





def search(request):

  st=request.GET.get('title')

  posts=Post.objects.filter(title__icontains=st)

  data={

    'posts':posts

  }

  return render(request,'search.html',data)






def post(request, url):
    post= Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, "posts.html", {'post':post,'cats':cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts= Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat':cat,'posts': posts})