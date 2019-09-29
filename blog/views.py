from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

dummy_content = Post.objects.all()

def home(request):
    context = {
        'posts': dummy_content,
        'title': 'Home Page'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

# Create your views here.
