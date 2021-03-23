from django.db import models

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
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()