from django.shortcuts import render
from .models import Hotel

# Create your views here.


def homebage(request):
    all_hotels = Hotel.objects.all()
    return render(request,'all.html',{'all_hotels':all_hotels})
    

def details(request , id):
    
    hotel_detail = Hotel.objects.get(id=id)

    return render(request, 'detail.html', {'hotel_detail':hotel_detail})
