from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()  

    def delete_category(self):
        self.delete()      

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()    

    def delete_location(self):
        self.delete()
        
    @classmethod
    def get_location(cls):
        locations = Location.objects.all()
        return locations


class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id):
       cls.objects.filter(id=id).update(image)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location 
        
           