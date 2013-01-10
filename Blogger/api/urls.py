from django.conf.urls import patterns, include, url


urlpatterns = patterns('Blogger.api.views',
	url(r'^posts/$', 'posts', name='all_posts'),
)	