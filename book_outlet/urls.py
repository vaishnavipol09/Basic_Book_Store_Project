from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path("" , views.index),
    path("<int:id>" , views.book_detail, name="book-detail"),
]
