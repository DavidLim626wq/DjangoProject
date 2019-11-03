from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    #fields in the database
    tmstmp = datetime.now().strftime("%y%m%d%H%M%S")
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, editable=False)

    def get_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 2
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()
        super(Post, self).save(*args, **kwargs)

    def commentIsApproved(self):
        return self.comments.filter(isApproved=True)

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
