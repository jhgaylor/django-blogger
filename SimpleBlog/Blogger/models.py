from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType

entry_type = ContentType.objects.get(model='post')

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    #property for admin panel
    def number_of_uses(self):
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

    #property for admin panel
    def number_of_posts(self):
        return self.post_set.count()
    number_of_posts.short_description = "Number of posts"

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('author_archive', args=['-'.join([self.first_name, self.last_name])])
            

#http://stackoverflow.com/questions/8215570/ordering-entries-via-comment-count-with-django
#https://docs.djangoproject.com/en/dev/topics/db/managers/#custom-managers-and-model-inheritance
class PostManager(models.Manager):
    def get_query_set(self):
        return super(PostManager,self).get_query_set().all().extra(select={
                'comment_count': """SELECT COUNT(*) FROM django_comments
                    WHERE django_comments.object_pk = Blogger_post.id
                    AND django_comments.content_type_id = %s"""
            }, select_params=(entry_type.id,)).order_by('-comment_count')

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

    #property for admin panel
    def get_tags(self):
        names = ', '.join([t.name for t in self.tags.all()])
        if len(names) > 20:
            names = names[:20] + "..."
        return names
    get_tags.short_description = "Tags"
    

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.slug)])


