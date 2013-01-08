from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from Blogger.settings import BLOG_SETTINGS
from django.db.models import Sum
from Blogger.managers import PostManager
from django.contrib.syndication.views import Feed
import unidecode
import re

class Tag(models.Model):
    """
    A string to be associated with another model
    """
    
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_archive', args=[str(self.slug)])

    def number_of_uses(self):
        """Return count of post_set"""
        return self.post_set.count()
    number_of_uses.short_description = "Number of uses"


class Author(models.Model):
    """
    Association of a Blog Author data and a django user
    """

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (("first_name", "last_name"))    

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('author_archive', args=['-'.join([self.first_name, self.last_name])])

    def number_of_posts(self):
        """Return count of post_set"""
        return self.post_set.count()
    number_of_posts.short_description = "Number of posts"

class Post(models.Model):
    """
    User generated blog post
    """

    author = models.ForeignKey(Author, blank=True)
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=BLOG_SETTINGS['auto_publish']) #TODO: i don't think this is working.  would like to make it work.
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    objects = models.Manager() # The default manager.
    popular_posts = PostManager()

    class Meta:
        verbose_name_plural = "posts"

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.slug)])

    def get_tags(self):
        """Returns tags as a composite string"""
        names = ', '.join([t.name for t in self.tags.all()])
        if len(names) > 20:
            names = names[:20] + "..."
        return names
    get_tags.short_description = "Tags"

    #slug field should remove the need for this.  Leaving it here for a while until I'm sure
    # def set_slug(self):
    #     """Sets self.slug from self.title"""
    #     title_str = unidecode.unidecode(self.title).lower()
    #     self.slug = re.sub(r'\W+','-',title_str)
