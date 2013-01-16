django-blogger
===============

A simple blogging app for django.

Installation and setup
----------------------
Install from pypi

```
pip install django-blogger
```

Configure Django
* add (r'^', include('blogger.urls')), to your project's urls.py
* Make sure django.contrib.comments, django.contrib.markup, and django.contrib.admin are setup/enabled
* Ensure that 'rest_framework' is in your installed apps (currently the api is not easily severed from the package). 
* make changes to settings.py.  It should look something like this.


```
INSTALLED_APPS += ('blogger.themes.default', 'blogger')

TEMPLATE_CONTEXT_PROCESSORS += ("blogger.context_processors.blog_info",)

BLOG_SETTINGS = {
    'defaults': {
        'auto_publish': False,
        'auto_promote': False,
    },
    'info': {
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

1. Make an author and associate it with your django user
2. Post stuff!


Settings
--------
```
BLOG_SETTINGS = {
    'defaults': {
        'auto_publish': False,
    },
    'info': {
        'BLOG_TITLE': 'My Blog Name',
        'BLOG_SUBTITLE': 'Blog subname',
    } 
}
```

info is attached to all responses so the information is available to the templates.
defaults change the defaults of models and some constats for views

Themes
------
Themes are contained in blogger/themes/THEMENAME/
Temeplate files for themes are at blogger/themes/THEMENAME/templates/
Files include base.html, list.html, and view_post.html
Not all files are necessary as the app will fall back on blogger/themes/FALLBACK_THEME/templates/FILE.html where FALLBACK_THEME is the last theme in INSTALLED_APPS
Static files for themes are at blogger/themes/THEMENAME/static/
The default themes are default, 3col and 4col.  They all rely on bootstrap and jquery.


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
