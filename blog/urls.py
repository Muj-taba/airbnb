from django.urls import path 
from .views import all_blog , blog_details

app_name = 'blog' 

urlpatterns = [

    path('', all_blog, name='all_blog' ),
    path('<int:id>', blog_details, name="all_blog"),
]