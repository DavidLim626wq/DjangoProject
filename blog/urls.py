from django.urls import path
from .views import PostListView, PostDetailView, PostDetailJsonView, PostPlusForm
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from users import views as user_views

urlpatterns = [
    path('', PostListView.as_view(), name ='blog-home'),
    path('post/<int:pk>/', PostPlusForm.as_view(), name="post-detail"),
    path('about/', views.about, name ='blog-about'),
    path('posts/<int:pk>/', views.PostDetailJsonView.as_view(), name="post-json-detail"),
]
