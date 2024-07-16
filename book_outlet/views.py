from django.shortcuts import get_object_or_404, render # type: ignore

from .models import Book
from django.db.models import Avg # type: ignore

# Create your views here.

def index(request):
        books = Book.objects.all().order_by("-title") # in decending order
        num_books = books.count()
        avg_rating = books.aggregate(Avg("rating"))

        return render(request, 'book_outlet/index.html' , {
        "books": books,
        "total_numbers_of_books" : num_books,
        "average_rating" : avg_rating
    })


def book_detail(request,slug):
    # try:
    #  book = Book.objects.get(pk=id)
    
    # except: 
    #  raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request ,"book_outlet/book_detail.html",{
        "title" : book.title,
        "author" : book.author,
        "rating" : book.rating,
        "is_best_seller" :book.is_best_selling
    })       
