from django.contrib import admin

# Register your models here.
from .models import Post, Author, Comment, Request, Like
from api.user.models import User
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Request)
admin.site.register(Like)