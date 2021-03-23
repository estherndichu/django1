from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def photos(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category =  Category.objects.all()
    return render(request,'photos/index.html',{'images':images,'location':location,'category':category})