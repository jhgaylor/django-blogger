from django.conf import settings

def blog_info(request):
	return settings.BLOG_INFO