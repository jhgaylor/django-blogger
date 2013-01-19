from django.test import TestCase
from rest_framework.reverse import reverse


class ViewTests(TestCase):

    def setUp(self):
        #make a bunch of objects for the tests
        pass

    def test_api_root(self):
        resp = self.client.get(reverse('api_root'))
        self.assertEqual(resp.status_code, 200)

    def test_api_posts_list(self):
        resp = self.client.get(reverse('posts-list'))
        self.assertEqual(resp.status_code, 200)

    def test_api_post_detail(self):
        resp = self.client.get(reverse('post-detail'))
        self.assertEqual(resp.status_code, 200)

    def test_api_authors_list(self):
        resp = self.client.get(reverse('authors-list'))
        self.assertEqual(resp.status_code, 200)

    def test_api_author_detail(self):
        resp = self.client.get(reverse('author-detail'))
        self.assertEqual(resp.status_code, 200)

    def test_all_archive(self):
        resp = self.client.get(reverse('all_archive'))
        self.assertEqual(resp.status_code, 200)

    def test_yearly_archive(self):
        year = 2013
        resp = self.client.get(reverse('yearly_archive', kwargs={'year':year}))
        self.assertEqual(resp.status_code, 200)

    def test_monthly_archive(self):
        year = 2013
        month = 1
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

    #ensure that when a comment is creator, the poster
    #is redirected to the post they commented on
    #pass a ?c=1 (GET)
    def test_comment_posted(self):
        resp = self.client.get(reverse('comment_posted'), data={'c':1})
        self.assertEqual(resp.status_code, 200)

    def test_view_post(self):
        resp = self.client.get(reverse('view_post'))
        self.assertEqual(resp.status_code, 200)

    # don't test the validity, just the response code
    # def test_rss_feed_renders(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)
