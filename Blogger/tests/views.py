from django.test import TestCase
from rest_framework.reverse import reverse
from ..models import Author, Post
from django.contrib.auth.models import User
from django.contrib.comments import Comment
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now

class ViewTests(TestCase):

    def setUp(self):
        #make a bunch of objects for the tests
        password = 'test'
        test_admin = User.objects.create_superuser('test', 'test@codegur.us',
                                                   password)
        test_admin.first_name="Test"
        test_admin.last_name="Tester"
        test_admin.save()
        
        self.client.login(username=test_admin.username, password=password)

        post = Post.objects.create(
            author=test_admin,
            title="test post title",
            body="test post body",
            slug="test-post-title"
        )
        
    def test_api_root(self):
        resp = self.client.get(reverse('api_root'))
        self.assertEqual(resp.status_code, 200)

    def test_api_posts_list(self):
        resp = self.client.get(reverse('posts-list'))
        self.assertEqual(resp.status_code, 200)

    def test_api_post_detail(self):
        resp = self.client.get(reverse('post-detail', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_api_authors_list(self):
        resp = self.client.get(reverse('authors-list'))
        self.assertEqual(resp.status_code, 200)

    def test_api_author_detail(self):
        resp = self.client.get(reverse('author-detail', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_all_archive(self):
        resp = self.client.get(reverse('all_archive'))
        self.assertEqual(resp.status_code, 200)

    def test_yearly_archive(self):
        year = now().year
        resp = self.client.get(reverse('yearly_archive', kwargs={'year':year}))
        self.assertEqual(resp.status_code, 200)

    def test_monthly_archive(self):
        year = now().year
        month = str(now().month)
        # month has to be a 2 digit int represented as a string
        if len(month) == 1:
            month = "".join(['0', month])
        resp = self.client.get(reverse('monthly_archive', kwargs={'year':year, 'month':month}))
        self.assertEqual(resp.status_code, 200)

    def test_tag_archive(self):
        tag_string = "testtag"
        resp = self.client.get(reverse('tag_archive', kwargs={'tag': tag_string}))
        self.assertEqual(resp.status_code, 200)

    def test_author_archive(self):
        author_string = "Testy-Testington"
        resp = self.client.get(reverse('author_archive', kwargs={'author':author_string}))
        self.assertEqual(resp.status_code, 200)

    #ensure that when a comment is created that
    #the page redirects to the post commented on
    def test_comment_posted(self):
        comment = Comment.objects.create(
            id=1,
            object_pk=1,
            site_id=1,
            content_type = ContentType.objects.get(model='post')
        )
        resp = self.client.get(reverse('comment_posted'), data={'c':1})
        self.assertEqual(resp.status_code, 302)

        resp = self.client.get(reverse('comment_posted'), data={'c':1}, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_post(self):
        slug = "test-post-title"
        resp = self.client.get(reverse('view_post', kwargs={'slug':slug}))
        self.assertEqual(resp.status_code, 200)

    def test_rss_feed_renders(self):
        resp = self.client.get(reverse('latest_entries_rss'))
        self.assertEqual(resp.status_code, 200)
