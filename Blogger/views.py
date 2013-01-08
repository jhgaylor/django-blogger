from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from Blogger.models import Post, Tag, Author
from django.db.models import Sum
from django.contrib import messages
from django.contrib.comments import Comment
import datetime

from Blogger import settings as blogger_settings

def get_sidebar_data():
    popular_posts = Post.popular_posts.all()[:5] #use this for the proper way when implemented
    recent_posts = Post.objects.filter(published=True).order_by('-created_at')[:5]
    archive = Post.objects.all().dates('created_at','month',order='DESC')
    tags = Tag.objects.all()
    authors = Author.objects.all()
    data = {
        'popular_posts': popular_posts,
        'recent_posts': recent_posts,
        'archive': archive,
        'tags': tags,
        'authors': authors,
    }
    return data

def render_on_list(request, data):
    #this is a way to do themeing
    #print blogger_settings.BLOG_THEME_NAME + '/list.html'
    return render_to_response(blogger_settings.BLOG_THEME['template_path'] + '/list.html', data, context_instance=RequestContext(request))
    #return render_to_response('themes/3col/list.html', data, context_instance=RequestContext(request))

def comment_posted(request):
    
    c = request.GET['c']
    messages.add_message(request, messages.SUCCESS, 'Commented added successfully.')
    c = Comment.objects.get(pk=c)
    return redirect(c.content_object)

# Create your views here.
def list(request, year=None, month=None, tag=None, author=None):
    
    sidebar_data = get_sidebar_data()
    
    data = {
            'posts': None,
            'section_title': 'Posts'
        }

    data.update(sidebar_data)

    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        data['posts'] = posts
        data['section_title'] = "Posts"
        return render_on_list(request, data)
    if author:
        fname, lname = author.split('-')
        posts = Post.objects.filter(author__first_name=fname, author__last_name=lname)
        data['posts'] = posts
        data['section_title'] = "Posts"
        return render_on_list(request, data)
    if not year:
        posts = Post.objects.all().order_by('-created_at')
        data['posts'] = posts
        data['section_title'] = "Posts"
        return render_on_list(request, data)
        #Recent posts reverse chrono
    if not month:
        posts = Post.objects.filter(created_at__year=year).order_by('-created_at')
        data['posts'] = posts
        data['section_title'] = "Yearly Archive"
        return render_on_list(request, data)
    else:
        posts = Post.objects.filter(created_at__year=year).filter(created_at__month=month).order_by('-created_at')
        data['posts'] = posts
        data['section_title'] = "Monthly Archive"
        return render_on_list(request, data)
    

def view_post(request, slug):
    
    post = Post.objects.get(slug=slug)
    sidebar_data = get_sidebar_data()
    data = {
        'post': post,
    }
    data.update(sidebar_data)
    return render_to_response('view_post.html', data, context_instance=RequestContext(request))

def archive_time(request):
    pass

def archive_category(request, category=None):
    pass

def archive_author(request, author=None):
    pass


    