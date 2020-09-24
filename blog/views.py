from django.shortcuts import render
from .models import Blog

# Create your views here.


def all_blog(request):
    all_post = Blog.objects.all()
    return render (request, 'all_post.html', {'all_post':all_post})



def blog_details(request, id):
    post_detail = Blog.objects.get(id=id)
    return render(request,'post_detail.html',{'post_detail':post_detail})


def add_post(request):
    pass



def edit_post(request):
    pass