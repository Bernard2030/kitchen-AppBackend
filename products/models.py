from django.db import models
from cloudinary.models import CloudinaryField
from django.core.files import File

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name  

    def get_absolute_url(self):
        return f'/{self.slug}'     


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image') 
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name   

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url

        return ''                