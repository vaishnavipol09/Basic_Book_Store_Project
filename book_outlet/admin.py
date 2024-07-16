from django.contrib import admin # type: ignore

from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("author", "rating",)
    list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)

