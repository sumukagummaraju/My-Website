
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mysite/index.html')

def portfolio(request):
    return render(request,'mysite/portfolio.html')

def gallery(request):
    return render(request,'mysite/gallery.html')

def contact(request):
    return render(request,'mysite/contact.html')

