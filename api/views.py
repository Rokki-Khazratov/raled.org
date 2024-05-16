from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product




class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()

        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset




class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name=name)
        if category:
            queryset = queryset.filter(category=category)

        return queryset 

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
