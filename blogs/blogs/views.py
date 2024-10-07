from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

# def blog(request):
#     return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
