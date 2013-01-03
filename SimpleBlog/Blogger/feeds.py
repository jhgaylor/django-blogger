from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from Blogger.models import Post

class LatestEntriesFeed(Feed):
    title = "Blog RSS"
    link = "/rss/"
    description = "Updates on changes and additions to this blog."

    def items(self):
        return Post.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('view_post', args=[item.slug])
