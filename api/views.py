from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from api.models import *


def index(request):
    news = News.objects.all().order_by('-created_at')[:4]

    # Если форма отправлена (POST-запрос)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('tell')
        book_name = request.POST.get('kitobnomi')
        print(name)
        print(phone)
        print(book_name)
        if name and phone and book_name:
            BookOrder.objects.create(name=name, phone=phone, book_name=book_name)
            return HttpResponse("Buyurtmangiz muvaffaqiyatli qabul qilindi!")
        else:
            return HttpResponse("Iltimos, barcha maydonlarni to'ldiring.")

    # Контекст для шаблона
    context = {
        'news': news,
    }
    
    return render(request, 'index.html', context)



def news_detail(request,news_id):
    news_detail = News.objects.get(id=news_id)
    return render(request, 'news_detail.html', {'news_detail':news_detail})

def books(request):
    book_list = Product.objects.all()
    paginator = Paginator(book_list, 7) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'book' : book_list,
        'paginator' : paginator,
        'page_number' : page_number,
        'page_obj' : page_obj,
    }
    return render(request, 'books.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def history(request):
    history = History.objects.all().first()  
    return render(request, 'history.html', {'history': history})

def all_news(request):
    news = News.objects.all()
    return render(request, 'all_news.html', {'news': news})

def all_books(request):
    books = Product.objects.all()
    return render(request, 'all_books.html', {'books': books})


def book_detail(request,book_id):
    book = Product.objects.get(id=book_id)
    return render(request, 'book_detail.html',{'book':book})

def detail(request):
    return render (request,'detail.html',{'detail':detail})

def contact(request):
    contact = About.objects.all()
    return render(request, 'contact.html', {'contact':contact})


def member(request):
    member = Member.objects.all()
    return render(request, 'member.html',{'member':member})

def send(request):
    return render(request, 'send.html')