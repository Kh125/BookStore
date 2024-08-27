from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import Author
from ..serializers import AuthorSerializer

@api_view(['GET', 'POST'])
def author(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, status= status.HTTP_200_OK, safe=False)
    
    else:
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def author_with_id(request, id):
    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        return JsonResponse({'Error': 'No Author with this id.'}, status=status.HTTP_404_NOT_FOUND, safe=False)
    
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    
    else:
        author.delete()
        return JsonResponse({'Message': 'Successfully deleted.'}, status=status.HTTP_204_NO_CONTENT, safe=False)