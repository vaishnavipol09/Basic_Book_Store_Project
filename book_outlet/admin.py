from django.contrib import admin # type: ignore

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Book, BookAdmin)
