from django.test import TestCase
from ..models import Author, Post
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from ..feeds import LatestEntriesFeed

#test the feed https://github.com/Fantomas42/django-blog-zinnia/blob/master/zinnia/tests/feeds.py#L141
class TestFeeds(TestCase):

    def setUp(self):
        #make a bunch of objects for the tests
        password = 'test'
        test_admin = User.objects.create_superuser('test', 'test@test.com',
                                                   password)
        test_admin.first_name = "Test"
        test_admin.last_name = "Tester"
        test_admin.save()

        self.client.login(username=test_admin.username, password=password)

        Post.objects.create(
            author=test_admin,
            title="test post title",
            body="test post body",
            slug="test-post-title"
        )

    def test_latest_entries(self):
        
        feed = LatestEntriesFeed()
        self.assertEquals(feed.link, '/rss/')
        self.assertEquals(len(feed.items()), 1)
        self.assertEquals(feed.title, _("Blog RSS"))
        self.assertEquals(
            feed.description,
            _('Updates on changes and additions to this blog.'))