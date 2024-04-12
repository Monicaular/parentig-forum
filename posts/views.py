from django.shortcuts import render
from django.http import HttpResponse

def my_post(request):
    return HttpResponse("Hello, Post!")
