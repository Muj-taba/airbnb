from django.shortcuts import render
from .models import Blog
from .form import BlogForm

# Create your views here.


def all_blog(request):
    all_post = Blog.objects.all()
    return render (request, 'all_post.html', {'all_post':all_post})



def blog_details(request, id):
    post_detail = Blog.objects.get(id=id)
    return render(request,'post_detail.html',{'post_detail':post_detail})


def add_post(request):
    
    if request.method=='POST':
        pass
    else:
        form = BlogForm()
    return render(request,'add.html',{'form':form})



def edit_post(request):
    pass