from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Blogger.models import Post, Tag, Author

# Create your views here.
def list(request, year=None, month=None):
    if not year:
        posts = Post.objects.all()
        data = {
            'posts': posts,
        }
        return render_to_response('list.html', data, context_instance=RequestContext(request))
        return HttpResponse("Recent posts reverse chrono")    
    if not month:
        return HttpResponse("Year archive reverse chrono")
    else:
        return HttpResponse("Month archive reverse chrono")
    

def view_post(request, slug):
    
    post = Post.objects.get(slug=slug)
    data = {
        'post': post,
    }
    return render_to_response('view_post.html', data, context_instance=RequestContext(request))

def archive_time(request):
    pass

def archive_category(request, category=None):
    pass

def archive_author(request, author=None):
    pass


    