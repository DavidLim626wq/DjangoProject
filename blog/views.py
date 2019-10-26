from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Post, Comment
from .serializers import PostSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from .forms import CommentForm
from django.urls import reverse

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

class PostPlusForm(FormMixin, DetailView):
#a View contining post+form
    template_name = 'blog/post_detail.html'
    model = Post
    form_class = CommentForm


    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostPlusForm, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.save()
        return super(PostPlusForm, self).form_valid(form)


class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        content = JSONRenderer().render(serializer.data)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

class PostDetailJsonView(APIView):

    def get(self, request, pk):
        posts = Post.objects.get(id = pk)
        serializer = PostSerializer(posts)
        return JsonResponse(serializer.data, safe=False)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def my_view(request):
    data = {}
    return JsonResponse(data)

# Create your views here.
