from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import Inventory
from ..serializers import InventorySerializer

@api_view(['GET', 'POST'])
def inventory(request):
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return JsonResponse(serializer.data, status= status.HTTP_200_OK, safe=False)
    
    else:
        serializer = InventorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def inventory_with_id(request, id):
    try:
        inventory = Inventory.objects.get(pk=id)
    except Inventory.DoesNotExist:
        return JsonResponse({'Error': 'No inventory with this id.'}, status=status.HTTP_404_NOT_FOUND, safe=False)
    
    if request.method == 'GET':
        serializer = InventorySerializer(inventory)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = InventorySerializer(inventory, request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    else:
        Inventory.delete()
        return JsonResponse({'Message': 'Successfully deleted.'}, status=status.HTTP_204_NO_CONTENT, safe=False)