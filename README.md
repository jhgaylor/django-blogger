django-simple-blog
==================

A simple blogging app for django.

Installation and setup
----------------------
1. pip install django-blogger
2. Configure Django
  * TEMPLATE_CONTEXT_PROCESSORS += ("Blogger.context_processors.blog_info",)
  * INSTALLED_APPS += ('Blogger',)
  * Make sure django.contrib.comments, django.contrib.markup, and django.contrib.admin are setup/enabled
  * add (r'^', include('Blogger.urls')), to your project's urls.py
3. ./manage.py syncdb
  
First use
---------
In the django admin panel:

1. Make an author and associate it with your django user
2. Post stuff!


Settings
--------
Currently live in Blogger/settings.py (Needs to change, anyone got a better way?)
BLOG_INFO is attached to all responses so the information is available to the templates.
BLOG_SETTINGS change the defaults of models and some constats for views
BLOG_THEME controls which theme is currently active

Themes
------
Themes are contained in Blogger/templates/themes/THEMENAME/
Files include base.html, list.html, and view_post.html
Not all files are necessary, and the app will fall back on Blogger/templates/themes/FILE.html
Static files for themes are at Blogger/static/blogger_themes/THEMENAME/
The default themes are default, 3col and 4col.  They all rely on bootstrap and jquery.
If you know a better way to support themeing, please let me know!

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
