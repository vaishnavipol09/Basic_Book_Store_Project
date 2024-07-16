
from django.core import validators # type: ignore
from django.db import models # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator # type: ignore
from django.urls import reverse # type: ignore
#from django.utils.text import slugify # type: ignore

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") 
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="" ,blank=True,  null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail",  args=[self.id])
    
    #def save(self, *args, **kwargs):
      #  self.id = slugify(self.title)
      #  super().save(*args, **kwargs)

    

def __str__(self):
    return f"{self.title} ({self.author})"