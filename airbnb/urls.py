from django.urls import path 
from .views import homebage , details

app_name = 'airbnb'

urlpatterns = [

    path('', homebage , name='homepage'),
    path('<int:id>/', details, name='details' )
]