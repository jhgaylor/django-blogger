from django.conf.urls import patterns, include, url
from Blogger.feeds import LatestEntriesFeed

urlpatterns = patterns('Blogger.views',
	url(r'^$', 'list', name='all_archive'),
    url(r'^(?P<year>\d{4})/$', 'list',name="yearly_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'list', name="monthly_archive"),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'list', name='tag_archive'),
    url(r'^author/(?P<author>[\w-]+)/$', 'list', name='author_archive'),
    url(r'^confirm/comment/$', 'comment_posted', name='comment_posted'),
    url(r'^post/(?P<slug>[\w-]+)/$', 'view_post', name='view_post'),
    (r'^rss/$', LatestEntriesFeed()),
)	