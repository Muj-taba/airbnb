from django.urls import path 
from .views import blogz

app_name = 'blog' 

urlpatterns = [

    path('home', blogz )
]