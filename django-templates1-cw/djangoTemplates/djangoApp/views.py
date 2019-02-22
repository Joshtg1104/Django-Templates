from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
# sets up link for index.html
def index(request):
    return render(request, 'djangoApp/Index.html')


# sets up link for base.html
def base(request):
    return render(request, 'djangoApp/base.html')


# sets up link for about.html
def about(request):
    return render(request, 'djangoApp/about.html')
