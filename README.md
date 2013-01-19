django-blogger
===============

A simple blogging app for django.

Install
------------
Install from pypi

```
pip install django-blogger
```

Configure Django
----------------

add to urls.py

```(r'^', include('blogger.urls')),``` 


settings.py
```
INSTALLED_APPS += (
    'django.contrib.admin', # This must be configured
    'django.contrib.comments', # This must be configured
    'django.contrib.markup', # to render markdown
    'rest_framework', # django rest framework 2
    'taggit', # django-taggit
    'blogger.themes.default', # the base theme
    'blogger' # the app
)

# this will attach BLOG_SETTINGS['info'] to HttpResponses
TEMPLATE_CONTEXT_PROCESSORS += ("blogger.context_processors.blog_info",)

BLOG_SETTINGS = {
    'defaults': { # change the defaults of models and some constats for views
        'auto_publish': False,
        'auto_promote': False,
    },
    'info': { # attached to all responses so the information is available to the templates.
        'BLOG_TITLE': 'My Blog Name',
        'BLOG_SUBTITLE': 'Blog subname',
    } 
}
```

Update the database
```
./manage.py syncdb
```


First use
---------
In the django admin panel:

1. Ensure your user has a first and last name
2. Post stuff!


Themes
------

```
blogger
+-- themes
    |-- default
    |   |-- static
    |   |   +-- Bootstrap
    |   |
    |   +-- templates
    |       |-- base.html
    |       |-- list.html
    |       +-- view_post.html
    |
    +-- 3col
        |-- static
        |   +-- Bootstrap
        |
        +-- templates
            |-- base.html
            |-- list.html
            +-- view_post.html
```

Not all files are necessary as the app will fall back on the last theme in INSTALLED_APPS


Features
--------
* RSS Feed 
* Markdown 
* Twitter Bootstrap UI
* Tags 
* Multiple Authors
* Archive 
* Comments
* Administration is done through auto generated admin
* read/write API

Example sites
-------------
http://codegur.us 
