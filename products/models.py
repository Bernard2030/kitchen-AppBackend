from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

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


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
  


    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.first_name 


class OderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)


    def __str__(self) -> str:
        return '%s' % self.id

