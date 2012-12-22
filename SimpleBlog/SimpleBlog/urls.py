from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleBlog.views.home', name='home'),
    # url(r'^SimpleBlog/', include('SimpleBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^list/', 'Blogger.views.list', name='list'),
    url(r'^posts/(?P<id>\d+)/', 'Blogger.views.view_post', name='view_post'),
)
