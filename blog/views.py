from django.shortcuts import render , redirect
from .models import Blog
from .form import BlogForm
from django.urls import reverse

# Create your views here.


def all_blog(request):
    all_post = Blog.objects.all()
    return render (request, 'all_post.html', {'all_post':all_post})



def blog_details(request, id):
    post_detail = Blog.objects.get(id=id)
    return render(request,'post_detail.html',{'post_detail':post_detail})


def add_post(request):
    
    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:all_blog'))

    else:
        form = BlogForm()
    return render(request,'add.html',{'form':form})


#
#def edit_post(request, id ):
 #   pass
 #   edit_post = Blog.objects.get(id=id)
  #  if request.method=='POST':
   #     form = BlogForm(request.POST, request.FILES)
    #    if form.is_valid():
     #       form.save()
      #      return redirect(reverse('blog:all_blog'))


   # else:
    #    form = BlogForm(instance=edit_post)
    #return render(request,'edit.html',{'form':form})

