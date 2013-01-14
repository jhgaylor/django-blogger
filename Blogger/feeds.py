from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from Blogger.models import Post, Tag
from django.utils.translation import ugettext_lazy as _


class LatestEntriesFeed(Feed):
    """RSS feed of the latest Posts"""
    title = _("Blog RSS")
    link = "/rss/"
    description = _("Updates on changes and additions to this blog.")

    def items(self):
        return Post.objects.order_by('-created_at')[:5]

    def item_author_name(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        author's name as a normal Python string.
        """
        return item.author

    def item_title(self, item):
        """Returns an item's title"""
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        pubdate.
        """
        return item.created_at

    def item_categories(self):
        """
        Returns the categories for every item in the feed.
        """
        return Tag.objects.all()

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        """Returns item URL"""
        return reverse('view_post', args=[item.slug])
