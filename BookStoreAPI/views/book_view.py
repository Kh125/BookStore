from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..services.book_service import (
    get_all_books, 
    get_book_by_id, 
    create_book, 
    update_book, 
    delete_book, 
    order_book_service
)
from ..serializers import BookSerializer, OrderSerializer
from ..utils import handle_exception
from django.core.exceptions import ValidationError

@api_view(['GET', 'POST'])
def book(request):
    if request.method == 'GET':
        try:
            books = get_all_books()
            serializer = BookSerializer(books, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return handle_exception(e)
    elif request.method == 'POST':
        try:
            data = create_book(request.data)
            return JsonResponse(data, status=status.HTTP_201_CREATED, safe=False)
        except ValidationError as e:
            return handle_exception(e.message, status_code=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_with_id(request, id):
    try:
        book = get_book_by_id(id)
    except ValidationError as e:
        return handle_exception(e.message, status_code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            data = update_book(book, request.data)
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except ValidationError as e:
            return handle_exception(e.message, status_code=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        delete_book(book)
        return JsonResponse({'Message': 'Successfully deleted.'}, status=status.HTTP_204_NO_CONTENT, safe=False)

@api_view(['POST'])
def order_book(request, book_id):
    try:
        user_id = request.data.get('user_id')
        quantity = request.data.get('quantity')
        
        new_order = order_book_service(user_id, book_id, quantity)
        order_serializer = OrderSerializer(new_order)
        
        return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED, safe=False)
    except ValidationError as e:
        return handle_exception(e.message, status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return handle_exception(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
