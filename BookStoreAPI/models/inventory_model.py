from django.db import models
from .book_model import Book

class Inventory(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(default=0)
    remaining_stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title}"