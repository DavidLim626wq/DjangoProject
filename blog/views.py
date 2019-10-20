from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer

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

class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        content = JSONRenderer().render(serializer.data)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def my_view(request):
    data = {}
    return JsonResponse(data)

# Create your views here.
