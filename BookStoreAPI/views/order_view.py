from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import Order
from ..serializers import OrderSerializer

@api_view(['GET', 'POST'])
def order(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, status= status.HTTP_200_OK, safe=False)
    
    else:
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def order_with_id(request, id):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return JsonResponse({'Error': 'No order with this id.'}, status=status.HTTP_404_NOT_FOUND, safe=False)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    else:
        order.delete()
        return JsonResponse({'Message': 'Successfully deleted.'}, status=status.HTTP_204_NO_CONTENT, safe=False)