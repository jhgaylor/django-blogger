from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleBlog.views.home', name='home'),
    # url(r'^SimpleBlog/', include('SimpleBlog.foo.urls')),

    (r'^', include('Blogger.urls')), #no $ on included urlconfs.  It would cause breakage
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^posts/(?P<id>\d+)/', 'Blogger.views.view_post', name='view_post'),
)
