from django.test import TestCase
from rest_framework.reverse import reverse


class ContextProcessorTest(TestCase):

    #make sure that the dictionary is added to the request
    def test_context(self):
        resp = self.client.get(reverse('all_archive'))
        self.assertIn('BLOG_TITLE', resp.context)
