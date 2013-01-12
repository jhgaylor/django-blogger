from rest_framework import serializers
from Blogger.models import Post, Author


class PostSerializer(serializers.HyperlinkedModelSerializer):


    author = serializers.HyperlinkedRelatedField(source='author', view_name='author-detail')
    #tags = serializers.ManyRelatedField(source='tags')

    class Meta:
        model = Post
        fields = ('url', 'author', 'title', 'body',
                  'created_at', 'published',
                  'slug')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('url', 'first_name', 'last_name')
