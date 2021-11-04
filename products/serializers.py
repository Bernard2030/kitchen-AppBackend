from rest_framework import serializers
from .models import Category,Product,Order,OderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ('id','name','description','price','get_image')


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id','name','get_absolute_url','products') 


class MyOderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OderItem
        fields = ('price','product','quantity',)


class MyOderSerializer(serializers.ModelSerializer):
    items = MyOderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id','firs_name','last_name','email','address','place','phone','items',)


class OderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OderItem
        fields = ('price','product','quantity',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','first_name','last_name','email','address','place','phone','items',)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OderItem.objects.create(order=order, **item_data)

        return order                                               