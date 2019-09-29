from django.shortcuts import render
from django.http import HttpResponse

dummy_content = [
    {
        'author':'Ron Vibbentrop',
        'title': 'Information',
        'content': 'ナニホム屋以あいこかゆふしくき瀬遊ヌロツて',
        'date_posted': 'Today'
    },
    {
        'author':'Harry McGoring',
        'title': 'Blog Post 2',
        'content': 'Лорем ипсум долор сит амет',
        'date_posted': 'Yesterday'
    },
]

def home(request):
    context = {
        'posts': dummy_content,
        'title': 'Home Page'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

# Create your views here.
