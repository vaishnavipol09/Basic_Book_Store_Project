from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path("" , views.index),
    path("<slug:slug>" , views.book_detail, name="book-detail"),
]
