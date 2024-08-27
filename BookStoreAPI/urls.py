from django.urls import path
from .views.author_view import author, author_with_id
from .views.book_view import book, book_with_id, order_book
from .views.inventory_view import inventory, inventory_with_id
from .views.publisher_view import publisher, publisher_with_id
from .views.order_view import order, order_with_id

urlpatterns = [
    path("authors/", author, name='author'),
    path("authors/<int:id>", author_with_id, name='author_with_id'),
    path("books/", book, name='book'),
    path("books/order/<int:book_id>", order_book, name='order_book'),
    path("books/<int:id>", book_with_id, name='book_with_id'),
    path("inventories/", inventory, name='inventory'),
    path("inventories/<int:id>", inventory_with_id, name='inventory_with_id'),
    path("publishers/", publisher, name='publisher'),
    path("publishers/<int:id>", publisher_with_id, name='publisher_with_id'),
    path("orders/", order, name='order'),
    path("orders/<int:id>", order_with_id, name='order_with_id')
]

