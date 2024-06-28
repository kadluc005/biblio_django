from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Borrow
from .form import BorrowForm
from biblio.settings import AUTH_USER_MODEL

# Create your views here.

def index(request):
    query = request.GET.get('search')
    if query:
        books = Book.objects.filter(book_title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'mybiblio/books.html', {'books': books})

def home(request):
    return render(request, 'base.html')

def detail(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(request, 'mybiblio/bookdetail.html', {'book': book})

@login_required
def borrow(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BorrowForm(request.POST, request.FILES)
        if form.is_valid:
            borrow = form.save(commit=False)
            borrow.user = request.user
            borrow.book_id = book
            borrow.save()
            messages.success(request, 'Book borrowed successfully!')
            form = BorrowForm()
            return render(request, 'mybiblio/borrows_page.html', {'form': form, 'book': book})
        else:
            messages.error(request, 'There was an error in your form.')
            return redirect('mybiblio/book_detail', book_id)
    else:
        form = BorrowForm()
        return render(request, 'mybiblio/borrows.html', {'form': form, 'book': book})
    

def user_borrows(request):
    borrows = Borrow.objects.filter(user = request.user)
    return render(request, 'mybiblio/borrows_page.html', {'borrows': borrows})