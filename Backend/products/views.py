from django.shortcuts import render
from products.models import Tag, Product, Brand, Category
from rest_framework import generics, status
from products import serializers 
from rest_framework import permissions
from django.db import IntegrityError
from rest_framework.response import Response


class TagViewsets(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            message = "An error occurred while creating the tag. Please make sure the tag name is unique."
            return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)

class ProductViewsets(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            message = "An error occurred while creating the Product. Please make sure the Product name is unique."
            return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)

class BrandViewset(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.BrandSerializer
    queryset = Brand.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            message = "An error occurred while creating the Brand. Please make sure the Brand name is unique."
            return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewset(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            message = "An error occurred while creating the Category. Please make sure the Category name is unique."
            return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)