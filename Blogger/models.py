from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from .managers import PostManager

BLOG_SETTINGS = settings.BLOG_SETTINGS['defaults']

class Author(User):
    class Meta:
        proxy=True

    def get_absolute_url(self):
        return reverse('author_archive',
                       args=['-'.join([self.first_name, self.last_name])])

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])


class Post(models.Model):
    """
    User generated blog post
    """

    author = models.ForeignKey(User, blank=True, verbose_name=_("author"))
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
