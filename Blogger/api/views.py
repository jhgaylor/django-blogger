from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from Blogger.models import Post, Tag, Author
from django.db.models import Sum
from django.contrib import messages
from django.contrib.comments import Comment
import datetime


def posts(request):

    posts = Post.objects.all()
    return HttpResponse("success")
