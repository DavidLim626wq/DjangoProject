from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

dummy_content = Post.objects.all()

'''
#function-based listView
def home(request):
    context = {
        'posts': dummy_content,
        'title': 'Home Page'
    }
    return render(request, 'blog/home.html', context)
'''

#Class-based listView
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
#to use class based views use <app>/<model>_<viewtype>.html
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

# Create your views here.
