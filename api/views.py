from django.shortcuts import render

from api.models import About, Partner, Product

def index(request):
    best_books = Product.objects.filter(best=True)
    partner = Partner.objects.all()
    context = {
        'best_books': best_books,
        'partner': partner,
    }
    return render(request, 'index.html', context)

def books(request):
    book = Product.objects.all()
    context = {
        'book' : book,
    }
    return render(request, 'books.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    contact = About.objects.all()
    return render(request, 'contact.html', {'contact':contact})