from django.conf.urls import patterns, include, url
from Blogger.feeds import LatestEntriesFeed

urlpatterns = patterns('',
	url(r'^$', 'Blogger.views.list', name='all_archive'),
    url(r'^(?P<year>\d{4})/$', 'Blogger.views.list',name="yearly_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'Blogger.views.list', name="monthly_archive"),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'Blogger.views.list', name='tag_archive'),
    url(r'^author/(?P<author>[\w-]+)/$', 'Blogger.views.list', name='author_archive'),
    url(r'^confirm/comment/$', 'Blogger.views.comment_posted', name='comment_posted'),
    url(r'^post/(?P<slug>[\w-]+)/$', 'Blogger.views.view_post', name='view_post'),
    (r'^rss/$', LatestEntriesFeed()),
)	