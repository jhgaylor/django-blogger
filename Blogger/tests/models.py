"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# from django.test import TestCase
# from .models import Post
# # from django.util import unittest


# class PostTests(TestCase):
#     def test_creation(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)


#make sure we can instantiate a django.auth.models.User through a blogger.models.Author proxy.
    #make sure get_absolute_url works
#can we create an author???

#create a post, save it, and assert the values are the same
    #get tags off a post, assert they are equal. the model save should do the tag breaking up for us... atleast it does through the admin panel.
    #assert that the model defaulted to the correct values for the boolean settigns
    #assert that slugify(title) == slug?
    #assert that author == user that created the post
