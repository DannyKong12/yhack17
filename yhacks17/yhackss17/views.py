from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def text(request, text):
    return HttpResponse(text)
