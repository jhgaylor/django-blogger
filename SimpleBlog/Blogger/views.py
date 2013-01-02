from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Blogger.models import Post, Tag, Author
from django.db.models import Sum
import datetime


# Create your views here.
def list(request, year=None, month=None, tag=None):
    popular_posts = Post.popular_posts.all() #use this for the proper way when implemented
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:5]
    archive = Post.objects.all().dates('created_at','month',order='DESC')
    tags = Tag.objects.all()
    data = {
            'posts': None,
            'popular_posts': popular_posts,
            'recent_posts': recent_posts,
            'archive': archive,
            'tags': tags,
            'section_title': 'Posts'
        }
    if tag:
        posts = Post.objects.filter(tags__name=tag)
        data['posts'] = posts
        data['section_title'] = "Posts"
        return render_to_response('list.html', data, context_instance=RequestContext(request))
    if not year:
        posts = Post.objects.all().order_by('-created_at')
        data['posts'] = posts
        data['section_title'] = "Posts"
        return render_to_response('list.html', data, context_instance=RequestContext(request))
        #Recent posts reverse chrono
    if not month:
        posts = Post.objects.filter(created_at__year=year).order_by('-created_at')
        data['posts'] = posts
        data['section_title'] = "Yearly Archive"
        return render_to_response('list.html', data, context_instance=RequestContext(request))
    else:
        posts = Post.objects.filter(created_at__year=year).filter(created_at__month=month).order_by('-created_at')
        data['posts'] = posts
        data['section_title'] = "Monthly Archive"
        return render_to_response('list.html', data, context_instance=RequestContext(request))
    

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


    