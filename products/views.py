from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product,Category,Order
from .serializers import ProductSerializer, CategorySerializer,OrderSerializer,MyOderSerializer
# for order class
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, authentication,permissions
from rest_framework.decorators import api_view,authentication_classes,parser_classes, permission_classes



# Create your views here.
class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category_slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self,request,category_slug, product_slug, format=None):
        product = self.get_object(category_slug,product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)  


class CategoryDetail(APIView):
    def get_object(self,category_slug):
      try:
          return Category.objects.get(slug=category_slug)
      except Category.DoesNotExist:
          raise Http404 

    def get(self,request,category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @api_view(['POST'])
    def search(request):
        query = request.data.get('query', '')

        if query:
            products = Product.objects.filter(Q(name_icontains=query)|Q(description_icontains=query)) 
            serializer = ProductSerializer(products, many=True)

            return Response(serializer.data)

        else:
            return Response({'products':[]})

# order views

class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, form=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOderSerializer(orders, many=True)

        return Response(serializer.data)


# def search(request, category_slug):
#     query = request.GET.get('q')
#     if query:
#         products = Product.objects.filter(Q(name_icontains=query)|Q(description_icontains=query)) 
#         serializer = ProductSerializer(products, many=True)

#         return render(request, 'products/search.html', {'products': serializer.data})
#     else:
#         return render(request, 'products/search.html', {'products': []})