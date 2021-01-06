from django.shortcuts import render
from .models import Author, Post

# Create your views here.
def index(response):
    return render(response, 'index.html', {})
