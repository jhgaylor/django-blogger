from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
#from blogger.settings import BLOG_SETTINGS
from django.conf import settings
from django.db.models import Sum
from blogger.managers import PostManager
from django.contrib.syndication.views import Feed
import unidecode
import re
from taggit.managers import TaggableManager

from django.utils.translation import ugettext_lazy as _
BLOG_SETTINGS = settings.BLOG_SETTINGS['defaults']

class Author(models.Model):
    """
    Association of a Blog Author data and a django user
    """

    first_name = models.CharField(max_length=200, verbose_name=_("first name"))
    last_name = models.CharField(max_length=200, verbose_name=_("last name"))
    user = models.ForeignKey(User, verbose_name=_("user"))

    class Meta:
        unique_together = (("first_name", "last_name"),)

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('author_archive',
                       args=['-'.join([self.first_name, self.last_name])])

    def number_of_posts(self):
        """Return count of post_set"""
        return self.post_set.count()
    number_of_posts.short_description = _("Number of posts")


class Post(models.Model):
    """
    User generated blog post
    """

    author = models.ForeignKey(Author, blank=True, verbose_name=_("author"))
    title = models.CharField(max_length=200, unique=True,
                             verbose_name=_("title"))
    body = models.TextField(verbose_name=_("body"))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_("created at"))
    published = models.BooleanField(default=BLOG_SETTINGS['auto_publish'],
                                    verbose_name=_("published?"))
    promoted = models.BooleanField(default=BLOG_SETTINGS['auto_promote'],
                                    verbose_name=_("promoted?"))
    tags = TaggableManager() #models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name=_("slug"))

    objects = models.Manager()  # The default manager.
    popular_posts = PostManager()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.slug)])

    def get_tags(self):
        """Returns tags as a composite string"""
        names = ', '.join([t.name for t in self.tags.all()])
        #if len(names) > 20:
        #    names = names[:20] + "..."
        return names
    get_tags.short_description = _("Tags")

    # slug field should remove the need for this.
    # Leaving it here for a while until I'm sure
    # def set_slug(self):
    #     """Sets self.slug from self.title"""
    #     title_str = unidecode.unidecode(self.title).lower()
    #     self.slug = re.sub(r'\W+','-',title_str)
