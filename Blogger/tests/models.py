from django.test import TestCase

from ..models import Author, Post
from django.contrib.auth.models import User






class ModelTests(TestCase):

    def setUp(self):
        #make a bunch of objects for the tests
        password = 'test'
        test_admin = User.objects.create_superuser('test', 'test@codegur.us',
                                                   password)
        test_admin.first_name = "Test"
        test_admin.last_name = "Tester"
        test_admin.save()

        self.client.login(username=test_admin.username, password=password)

        post = Post.objects.create(
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
        posts_count = Post.objects.all().count()
        self.assertEqual(p.id, posts_count)

    def test_post_unicode(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, str(post))

    def test_post_get_tags(self):
        post = Post.objects.get(pk=1)
        post.tags.set('a,b,c')
        self.assertEqual(post.get_tags(), 'a,b,c')


#make sure we can instantiate a django.auth.models.User through a blogger.models.Author proxy.
    #make sure get_absolute_url works
#can we create an author???

#create a post, save it, and assert the values are the same
    #get tags off a post, assert they are equal. the model save should do the tag breaking up for us... atleast it does through the admin panel.
    #assert that the model defaulted to the correct values for the boolean settigns
    #assert that slugify(title) == slug?
    #assert that author == user that created the post
