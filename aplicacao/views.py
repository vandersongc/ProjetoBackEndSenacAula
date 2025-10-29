from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')
def produtos(request):
    return render(request,'produtos.html')
def clientes(request):
    return render(request,'clientes.html')

# Create your views here.
