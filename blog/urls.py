from django.urls import path 
from .views import all_blog , blog_details , add_post , PostList ,DetailView

app_name = 'blog' 

urlpatterns = [



    #CBV
    path('cbv',PostList.as_view(), name='all_post_cbv'),
    path('cbv/<int:pk>',DetailView.as_view(), name='DetailView_cbv'),

    #FBV

    path('', all_blog, name='all_blog' ),
    path('add',add_post, name='add_post'),
    path('<int:id>', blog_details, name="blog_detail"),
    
]