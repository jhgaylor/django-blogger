from django.test import TestCase
from ..models import Author, Post

from django.contrib.auth.models import User


class ModelTests(TestCase):

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

    def test_post_new(self):
        author = User.objects.get(pk=1)
        p = Post()
        p.author=author
        p.title="test post title2"
        p.body="test post body"
        p.slug="test-post-title2"
        p.save()
        self.assertEqual(p, Post.objects.get(slug=p.slug))
        #self.assertEqual(p.published, BLOG_SETTINGS['defaults']['auto_publish'])
        #self.assertEqual(p.promoted, BLOG_SETTINGS['defaults']['auto_promote'])
        

    def test_author_url(self):
        author = Author.objects.get(pk=1)
        resp = self.client.get(author.get_absolute_url())
        self.assertEqual(resp.status_code, 200)

    def test_post_unicode(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, str(post))

    def test_post_get_tags(self):
        post = Post.objects.get(pk=1)
        post.tags.set('a,b,c')
        self.assertEqual(post.get_tags(), 'a,b,c')

    def test_author_create(self):
        author = Author.objects.create_user('author_test', 'author_test@test.come', 'test')
        self.assertEqual(author, Author.objects.get(username='author_test'))
