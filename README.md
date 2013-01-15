django-simple-blog
==================

A simple blogging app for django.

Installation and setup
----------------------

```
pip install django-blogger
```

2. Configure Django
	* add (r'^', include('Blogger.urls')), to your project's urls.py
 	* Make sure django.contrib.comments, django.contrib.markup, and django.contrib.admin are setup/enabled
    * Ensure that 'rest_framework' is in your installed apps (currently the api is not easily severed from the package). 
	* make changes to settings.py.  It should look something like this.


```
INSTALLED_APPS += ('Blogger.themes.default', 'Blogger')

TEMPLATE_CONTEXT_PROCESSORS += ("Blogger.context_processors.blog_info",)

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
Themes are contained in Blogger/themes/THEMENAME/
Temeplate files for themes are at Blogger/themes/THEMENAME/tempaltes/
Files include base.html, list.html, and view_post.html
Not all files are necessary, and the app will fall back on Blogger/templates/themes/FILE.html
Static files for themes are at Blogger/themes/THEMENAME/static/
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

Planned Additions
-----------------
* read/write API
