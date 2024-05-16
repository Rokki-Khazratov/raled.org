from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'language', 'url', 'thumb', 'category', 'date']

