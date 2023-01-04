from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
def tasklist(request):
    return HttpResponse('to do list')
