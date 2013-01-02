from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Blogger.models import Post, Tag, Author
from django.db.models import Sum

#only necessary on the hacky way
from django.contrib.contenttypes.models import ContentType
entry_type = ContentType.objects.get_for_model(Post)

# Create your views here.
def list(request, year=None, month=None):
    popular_posts = Post.popular_posts.all() #use this for the proper way when implemented
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:5]
    archive = None
    tags = Tag.objects.all()
    data = {
            'posts': None,
            'popular_posts': popular_posts,
            'recent_posts': recent_posts,
            'archive': archive,
            'tags': tags
        }
    if not year:
        posts = Post.objects.all().order_by('-created_at')
        data['posts'] = posts
        return render_to_response('list.html', data, context_instance=RequestContext(request))
        #Recent posts reverse chrono
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


    