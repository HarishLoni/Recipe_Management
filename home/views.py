from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home/index.html",context={'page':'Django2024'})

def about(request):
    context={'page':'about'}
    return render(request,"home/about.html",context)

def contact(request):
    context={'page':'contact'}
    return render(request,"home/contact.html",context)

