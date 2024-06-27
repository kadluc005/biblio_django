from django.db import models
from biblio.settings import AUTH_USER_MODEL

# Create your models here.

class Book(models.Model):
    book_image = models.ImageField(upload_to="images", blank=True, null=True)
    book_title = models.CharField(max_length=100)
    book_resume = models.TextField()
    book_author = models.CharField(max_length=100)
    book_publishing_date = models.DateField()
    
    def __str__(self) -> str:
        return self.book_title

class Borrow(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    return_date = models.DateField()