from django.shortcuts import render
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from store.models import Product, Category
from store.serializers import ProductSerializer, CategorySerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import filters
from .filters import ProductFilter

# class ProductViewSets(ViewSet):
#     def list(self, request):
#         all_products = Product.objects.all().order_by('name')
#         serializer = ProductSerializer(all_products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def retrieve(self, request, pk):
#         all_products = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(all_products)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def update(self, request, pk):
#         all_products = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(all_products, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def destroy(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class CategoryViewSets(ViewSet):
#     def list(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','price','category__name']
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price']
    ordering = ['name']


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']






