from django.conf import settings


def blog_info(request):
    """returns settings.BLOG_INFO"""
    return settings.BLOG_SETTINGS['info']
