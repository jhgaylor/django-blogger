from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

from django.db.models import Sum
from Blogger.managers import PostManager
from django.contrib.syndication.views import Feed
import unidecode
import re

# Create your models here.
class Tag(models.Model):

    """A model to associate a string with another model"""
    
    name = models.CharField(max_length=200)
    
    def number_of_uses(self):
        """Return count of post_set"""
        return self.post_set.count()
    number_of_uses.short_description = "Number of uses"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_archive', args=[str(self.name)])

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def number_of_posts(self):
        """Return count of post_set"""
        return self.post_set.count()
    number_of_posts.short_description = "Number of posts"

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('author_archive', args=['-'.join([self.first_name, self.last_name])])

class Post(models.Model):
    author = models.ForeignKey(Author, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=settings.BLOG_SETTINGS['auto_publish']) #TODO: i don't think this is working.  would like to make it work.
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.CharField(max_length=200, blank=True)
    
    objects = models.Manager() # The default manager.
    popular_posts = PostManager()

    class Meta:
        verbose_name_plural = "posts"

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.slug)])

    #validation
    # def clean_fields(self):
    #     pass

    # def clean(self):
    #     pass

    # def validate_unique(self):
    #     pass

    #property for admin panel
    def get_tags(self):
        """Returns tags as a composite string"""
        names = ', '.join([t.name for t in self.tags.all()])
        if len(names) > 20:
            names = names[:20] + "..."
        return names
    get_tags.short_description = "Tags"

    def set_slug(self):
        """Sets self.slug from self.title"""
        title_str = unidecode.unidecode(self.title).lower()
        self.slug = re.sub(r'\W+','-',title_str)
    

