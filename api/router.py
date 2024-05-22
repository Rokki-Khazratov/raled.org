from django.urls import path
from . import views
from django.urls import path
from .views import (
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
    Social_mediaRetrieveUpdateDestroyAPIView, 
    PartnerListCreateView, 
    PartnerRetrieveUpdateDestroyView, 
    OrgoniseListCreateView, 
    OrgoniseRetrieveUpdateDestroyView
)


urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-detail'),
    path('aboutus/', AboutListCreateAPIView.as_view(), name='aboutus-list-create'),
    path('aboutus/<int:pk>/', AboutRetrieveUpdateDestroyAPIView.as_view(), name='aboutus-detail'),
    path('workers/', WorkerListCreateAPIView.as_view(), name='worker-list-create'),
    path('workers/<int:pk>/', WorkerRetrieveUpdateDestroyAPIView.as_view(), name='worker-detail'),
    path('social_media/', Social_mediaListCreateAPIView.as_view(), name='social_media_list_create'),
    path('social_media/<int:pk>/', Social_mediaRetrieveUpdateDestroyAPIView.as_view(), name='social_media_detail'),
    path('partners/', PartnerListCreateView.as_view(), name='partner-list-create'),
    path('partners/<int:pk>/', PartnerRetrieveUpdateDestroyView.as_view(), name='partner-detail'),
    path('orgonise/', views.OrgoniseListCreateView.as_view(), name='orgonise-list-create'),
    path('orgonise/<int:pk>/', views.OrgoniseRetrieveUpdateDestroyView.as_view(), name='orgonise-detail'),
]
