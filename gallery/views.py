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
    return render(request, 'photos/location.html', {'location_images': images})   

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_image(category)
        message = f"{category}"
        return render(request, 'photos/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'photos/search.html', {"message": message})    