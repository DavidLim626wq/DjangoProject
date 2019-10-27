from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','email','isApproved','post')
    list_editable = ('isApproved',)

admin.site.register(Comment, CommentAdmin)
