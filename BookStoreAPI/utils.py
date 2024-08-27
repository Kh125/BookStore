from django.http import JsonResponse
from rest_framework import status

def handle_exception(ex, status_code=status.HTTP_400_BAD_REQUEST):
    return JsonResponse({'Error': str(ex)}, status=status_code, safe=False)
