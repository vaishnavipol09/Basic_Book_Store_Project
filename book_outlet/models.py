
from django.core import validators # type: ignore
from django.db import models # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator # type: ignore
from django.urls import reverse # type: ignore
from django.utils.text import slugify # type: ignore

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="" , null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail",  args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    

def __str__(self):
    return f"{self.title} ({self.rating})"