from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import Publisher
from ..serializers import PublisherSerializer

@api_view(['GET', 'POST'])
def publisher(request):
    if request.method == 'GET':
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True)
        return JsonResponse(serializer.data, status= status.HTTP_200_OK, safe=False)
    
    else:
        serializer = PublisherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def publisher_with_id(request, id):
    try:
        publisher = Publisher.objects.get(pk=id)
    except Publisher.DoesNotExist:
        return JsonResponse({'Error': 'No publisher with this id.'}, status=status.HTTP_404_NOT_FOUND, safe=False)
    
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = PublisherSerializer(publisher, request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    else:
        Publisher.delete()
        return JsonResponse({'Message': 'Successfully deleted.'}, status=status.HTTP_204_NO_CONTENT, safe=False)