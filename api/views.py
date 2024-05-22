from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def about_us(request):
    return render(request, 'about_us.html')