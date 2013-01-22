from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User

class ManagerTests(TestCase):

    def setUp(self):
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

    #test that the comment count is present on the queryset
    def test_comment_count(self):
        post = Post.popular_posts.get(pk=1)
        self.assertTrue(hasattr(post, 'comment_count'))
