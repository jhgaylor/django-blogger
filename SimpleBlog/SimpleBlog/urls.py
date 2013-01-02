from django.conf.urls import patterns, include, url
from Blogger.feeds import LatestEntriesFeed
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleBlog.views.home', name='home'),
    # url(r'^SimpleBlog/', include('SimpleBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'Blogger.views.list', name='all_archive'),
    url(r'^(?P<year>\d{4})/$', 'Blogger.views.list',name="yearly_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'Blogger.views.list', name="monthly_archive"),
    url(r'^tag/(?P<tag>[\w-]+)/$', 'Blogger.views.list', name='tag_archive'),
    url(r'^author/(?P<author>[\w-]+)/$', 'Blogger.views.list', name='author_archive'),
    url(r'^comment/posted/$', 'Blogger.views.comment_posted', name='comment_posted'),

    url(r'^post/(?P<slug>[\w-]+)/$', 'Blogger.views.view_post', name='view_post'),
    (r'^rss/$', LatestEntriesFeed()),


    
    url(r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    
    #url(r'^posts/(?P<id>\d+)/', 'Blogger.views.view_post', name='view_post'),
)
