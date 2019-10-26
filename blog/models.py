from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    #fields in the database
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    #fields to include
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    user = models.CharField(max_length=40) #get User's name
    email = models.EmailField(max_length=80)
    cmnt = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    isApproved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user
