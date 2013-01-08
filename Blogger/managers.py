from django.db import models
from django.contrib.contenttypes.models import ContentType
try:
	entry_type = ContentType.objects.get(model='post')
#http://stackoverflow.com/questions/8215570/ordering-entries-via-comment-count-with-django
#https://docs.djangoproject.com/en/dev/topics/db/managers/#custom-managers-and-model-inheritance
	class PostManager(models.Manager):

		"""A custom manager for Post models"""

		def get_query_set(self):
			"""attaches django comment_count to all querysets"""
			return super(PostManager,self).get_query_set().all().extra(select={
	                'comment_count': """SELECT COUNT(*) FROM django_comments
	                    WHERE django_comments.object_pk = Blogger_post.id
	                    AND django_comments.content_type_id = %s"""
	            }, select_params=(entry_type.id,)).order_by('-comment_count')
except:
	class PostManager(models.Manager):
		pass