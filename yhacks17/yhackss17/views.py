from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello, world. You're at the yhack(ss)17")
