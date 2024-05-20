from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import CategorySerializer, ProductSerializer, AboutSerializer, ContactSerializer, WorkerSerializer, Social_mediaSerializer, PartnerSerializer
from .models import Category, Product, Contact, About, Worker, Social_media, Partner

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .permission import IsAuth

class ExampleView(APIView):
    permission_classes = [IsAuth]

    def get(self, request, format=None):
        content = {
            'message': 'Hello, authenticated user!'
        }
        return Response(content)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuth]

    def get_queryset(self):
        queryset = Category.objects.all()

        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset



class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuth]

class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuth]
    pagination_class = CustomPageNumberPagination
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
    permission_classes = [IsAuth]


class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuth]

class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuth]



class AboutListCreateAPIView(ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAuth]


class AboutRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAuth]



class WorkerListCreateAPIView(ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAuth]

class WorkerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAuth]


class Social_mediaListCreateAPIView(ListCreateAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer
    permission_classes = [IsAuth]

class Social_mediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaSerializer
    permission_classes = [IsAuth]

class PartnerListCreateView(ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAuth]

class PartnerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAuth]
