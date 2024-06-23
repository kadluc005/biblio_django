from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'mybiblio/books.html', {'books': books})

def home(request):
    return render(request, 'base.html')