from django.urls import path
from . import views
from django.urls import path
from .api import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ContactListCreateAPIView, 
    ContactRetrieveUpdateDestroyAPIView, 
    AboutListCreateAPIView, 
    AboutRetrieveUpdateDestroyAPIView, 
    WorkerListCreateAPIView, 
    WorkerRetrieveUpdateDestroyAPIView, 
    Social_mediaListCreateAPIView, 
    Social_mediaRetrieveUpdateDestroyAPIView
)
from .views import *

urlpatterns = [
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('api/contacts/<int:pk>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-detail'),
    path('api/aboutus/', AboutListCreateAPIView.as_view(), name='aboutus-list-create'),
    path('api/aboutus/<int:pk>/', AboutRetrieveUpdateDestroyAPIView.as_view(), name='aboutus-detail'),
    path('api/workers/', WorkerListCreateAPIView.as_view(), name='worker-list-create'),
    path('api/workers/<int:pk>/', WorkerRetrieveUpdateDestroyAPIView.as_view(), name='worker-detail'),
    path('api/social_media/', Social_mediaListCreateAPIView.as_view(), name='social_media_list_create'),
    path('api/social_media/<int:pk>/', Social_mediaRetrieveUpdateDestroyAPIView.as_view(), name='social_media_detail'),

    path('', index,name='index'),
    path('books/', books,name='books'),
    path('about_us/', about_us,name='about_us'),
    path('contact/', contact,name='contact'),
]
