from django.urls import path 
from .views import all_blog , blog_details , add_post 

app_name = 'blog' 

urlpatterns = [

    path('', all_blog, name='all_blog' ),
    path('add',add_post, name='add_post'),
    #path('<int:id>',edit_post,name='edit_post'),
    path('<int:id>', blog_details, name="blog_detail"),
    
]