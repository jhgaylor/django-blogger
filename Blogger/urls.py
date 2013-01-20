from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .feeds import LatestEntriesFeed
from .views import PostList, PostDetail, AuthorList, AuthorDetail

api_patterns = patterns('blogger.views',
    url(r'^$', 'api_root', name="api_root"),
    url(r'^posts/$', PostList.as_view(), name='posts-list'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^authors/$', AuthorList.as_view(), name='authors-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author-detail'),
)

# Format suffixes
api_patterns = format_suffix_patterns(api_patterns, allowed=['json', 'api'])

urlpatterns = patterns('blogger.views',
    url(r'^$', 'list', name='all_archive'),
    url(r'^(?P<year>\d{4})/$', 'list', name="yearly_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'list', name="monthly_archive"),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'list', name='tag_archive'),
    url(r'^author/(?P<author>[\w-]+)/$', 'list', name='author_archive'),
    url(r'^confirm/comment/$', 'comment_posted', name='comment_posted'),
    url(r'^post/(?P<slug>[\w-]+)/$', 'view_post', name='view_post'),
    
    (r'^api/', include(api_patterns)),  
)

urlpatterns += patterns('',
    url(r'^rss/$', LatestEntriesFeed(), name="latest_entries_rss"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)