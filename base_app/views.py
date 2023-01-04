from django.contrib import admin
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task



# Register your models here.
class TaskList(ListView):
    model = Task
