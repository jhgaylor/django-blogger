from django.test import TestCase
from rest_framework.reverse import reverse


class PostTests(TestCase):

    def test_api_root(self):
        resp = self.client.get(reverse('api_root'))
        self.assertEqual(resp.status_code, 200)

    def test_posts_list(self):
        resp = self.client.get(reverse('posts-list'))
        self.assertEqual(resp.status_code, 200)

    def test_post_detail(self):
        resp = self.client.get(reverse('post-detail'))
        self.assertEqual(resp.status_code, 200)

    def test_authors_list(self):
        resp = self.client.get(reverse('authors-list'))
        self.assertEqual(resp.status_code, 200)

    def test_author_detail(self):
        resp = self.client.get(reverse('author-detail'))
        self.assertEqual(resp.status_code, 200)

    def test_all_archive(self):
        resp = self.client.get(reverse('all_archive'))
        self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)

    # def test_api_root(self):
    #     resp = self.client.get(reverse('api_root'))
    #     self.assertEqual(resp.status_code, 200)
