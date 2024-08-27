from django.core.exceptions import ValidationError
from ..models import Book, Inventory, Order
from ..serializers import BookSerializer

def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    try:
        return Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise ValidationError("No book with this ID.")

def create_book(data):
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        raise ValidationError(serializer.errors)

def update_book(book, data):
    serializer = BookSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        raise ValidationError(serializer.errors)

def delete_book(book):
    book.delete()

def order_book_service(user_id, book_id, quantity):
    book = get_book_by_id(book_id)
    inventory = Inventory.objects.get(book=book)

    if inventory.stock_quantity < quantity:
        raise ValidationError("Not enough stock available!")

    inventory.remaining_stock -= quantity
    inventory.save()

    new_order = Order.objects.create(
        user_id=user_id,
        book=book,
        quantity=quantity,
        status='completed'
    )
    return new_order
