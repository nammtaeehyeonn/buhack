from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def aaa(request):
    return render(request, 'aaa.html')

def bbb(request):
    return render(request, 'bbb.html')

def ccc(request):
    return render(request, 'ccc.html')