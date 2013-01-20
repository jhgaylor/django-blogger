from django.template.defaultfilters import slugify
from rest_framework import serializers
from .models import Post, Author


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes the Post model"""
    author = serializers.HyperlinkedRelatedField(source='author', view_name=
                                                 'author-detail')
    tags = serializers.ManyRelatedField(source='tags')

    class Meta:
        model = Post
        fields = ('url', 'author', 'title', 'body',
                  'created_at', 'published', 'tags',
                  'slug')

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            # author is controlled by the view
            instance.title = attrs['title']
            instance.body = attrs['body']
            instance.published = attrs['published']
            # TODO: assign tags from json data
            # tags = [tag.trim() for tag in attrs['tags'].split(',')]
            # instance.tags.set(tags)
            instance.slug = slugify(attrs['title'])
            return instance
        return Post(**attrs)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes the Author model"""
    posts = serializers.ManyHyperlinkedRelatedField(source='post_set', view_name='post-detail')

    class Meta:
        model = Author
        fields = ('url', 'username','first_name', 'last_name', 'posts')
