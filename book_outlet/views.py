from django.shortcuts import render # type: ignore

from .models import Book

# Create your views here.

def index(request):
        books = Book.objects.all()
        return render(request, 'book_outlet/index.html' , {
        "books": books
    })


def book_detail(request, id):
    book = Book.objects.get(pk=id)   #pk means primary key
    return render(request, 'book_outlet/book_detail.html' , {
        "title" : book.title,
        "author" : book.author,
        "rating" : book.rating,
        "is_bestselling" : book.is_bestselling,
    })
