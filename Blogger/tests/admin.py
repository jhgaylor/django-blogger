from django.test import TestCase
from ..models import Author, Post
from django.contrib.auth.models import User


class AdminTests(TestCase):

    def setUp(self):
        #make a bunch of objects for the tests
        password = 'test'
        test_admin = User.objects.create_superuser('test', 'test@codegur.us',
                                                   password)
        test_admin.first_name = "Test"
        test_admin.last_name = "Tester"
        test_admin.save()

        self.client.login(username=test_admin.username, password=password)

    def test_entry_add_and_change(self):
        """Test the insertion of a Post"""
        
        post_data = {'title': u'New entry',
                     'body': u'BODY',
                     'slug': u'new-entry',
                     'tags': u'test',
                    }

        response = self.client.post('/admin/blogger/post/add/', post_data, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.count()>0, True)

        post = Post.objects.get(title="New entry")
        
        self.assertEquals(post.author, User.objects.get(pk=1))
