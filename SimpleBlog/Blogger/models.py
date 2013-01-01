from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    user = models.ForeignKey(User)

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])

class Post(models.Model):
    author = models.ForeignKey(Author, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=settings.BLOG_SETTINGS['auto_publish']) #TODO: i don't think this is working.  would like to make it work.
    tags = models.ManyToManyField(Tag, blank=True)

    def get_tags(self):
        names = ', '.join([t.name for t in self.tags.all()])
        if len(names) > 20:
            names = names[:20] + "..."
        return names
    get_tags.short_description = "Tags"
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.id)])

class Comment(models.Model):
    creator = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(Post)

