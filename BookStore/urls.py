from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def default_route(request):
    return HttpResponse("This is the book store backend API developed by Django.")

urlpatterns = [
    path('', default_route),
    path('admin/', admin.site.urls),
    path('api/v1/', include('BookStoreAPI.urls'))
]
