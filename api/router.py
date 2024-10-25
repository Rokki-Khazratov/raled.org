from django.urls import path
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('news/<int:news_id>', news_detail,name='news_detail'),
    
    path('members/', member,name='member'),
    path('history/', history,name='history'),
    path('all_news/', all_news,name='all_news'),
    path('all_books/', all_books,name='all_books'),

    path('about_us/', about_us,name='about_us'),
    path('contact/', contact,name='contact'),
    path('books/', books,name='books'),
    path('books/<int:book_id>', book_detail,name='book_detail'),
    path('send/', send,name='send'),
]
