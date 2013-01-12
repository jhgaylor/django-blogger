from rest_framework import serializers
from Blogger.models import Post, Author


class PostSerializer(serializers.HyperLinkedModelSerializer):

    author = serializers.RelatedField(source='author')
    tags = serializers.ManyRelatedField(source='tags')

    class Meta:
        model = Post
        fields = ('author', 'title', 'body',
                  'created_at', 'published',
                  'tags', 'slug')


class AuthorSerializer(serializers.HyperLinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name')
