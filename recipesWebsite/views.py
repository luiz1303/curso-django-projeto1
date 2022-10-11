from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home (request):
    return render(request, 'recipeswebsite/home.html')

def sobre (request):
    return HttpResponse('Uma linda string')

def contato (request):
    return HttpResponse('Uma linda string')
