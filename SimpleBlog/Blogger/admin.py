from django.contrib import admin
from Blogger.models import Tag, Post, Author, Comment
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)