import os
#the name of your theme
BLOG_THEME_NAME = '4col'

#You probably don't want to manually edit this.  We're going to use convention to handle themeing
BLOG_THEME = {
    'name': BLOG_THEME_NAME,
    'static_path': 'blogger_themes/'+BLOG_THEME_NAME, #no leading or trailing /
    'template_path': 'themes/'+BLOG_THEME_NAME,
    # 'absolute_path': os.path.join(SITE_ROOT, 'Blogger/templates/themes/'+BLOG_THEME_NAME+'/')
}

BLOG_INFO = {
    'BLOG_TITLE': 'My Blog Name',
    'BLOG_SUBTITLE': 'Blog subname',
    'BLOG_THEME_DIR': BLOG_THEME['static_path']
}

BLOG_SETTINGS = {
    'auto_publish': True, #as you can see from the admin page, this doesn't have an effect
}