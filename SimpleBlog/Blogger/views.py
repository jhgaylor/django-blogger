from django.http import HttpRequest
from django.shortcuts import render_to_response
from Blogger.models import Post, Tag, Author

# Create your views here.
def list(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render_to_response('list.html', data)

def view_post(request, id):
    post = Post.objects.get(pk=id)
    data = {
        'post': post,
    }
    return render_to_response('view_post.html', data)

def archive_time(request):
    pass

def archive_category(request, category=None):
    pass

def archive_author(request, author=None):
    pass