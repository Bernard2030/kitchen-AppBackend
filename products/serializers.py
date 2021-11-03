from django.db.models import fields
from rest_framework import serializers
from .models import Category,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ('id','name','description','price')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','products')        