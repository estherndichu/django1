from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def photos(request):
    images = Image.objects.all()
    locations = Location.get_location()
    category =  Category.objects.all()
    return render(request,'photos/index.html',{'images':images,'locations':locations,'category':category})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'photos/location.html', {'location_images': images})   