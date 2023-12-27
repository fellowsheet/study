from django.contrib import admin
from .models import Follower, Like, Comment, Post, Channel, Category, Author

admin.site.register(Follower)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Author)
