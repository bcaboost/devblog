from rest_framework import serializers

from blogs.models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'created_on', 'body']


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email','created_on', 'body']


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'meta', 'thumb', 'content', 'published']


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    full_post = serializers.HyperlinkedIdentityField(view_name='single_post_api', lookup_field='slug')

    class Meta:
        model = Blog
        fields = ['title', 'author', 'meta', 'thumb', 'created_on', 'views', 'full_post']
    
    def get_author(self, obj):
        return obj.author.username


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = CommentSerializer(read_only=True, many=True)
    comments_count = serializers.SerializerMethodField(method_name='get_comments_count')

    class Meta:
        model = Blog
        fields = ['title', 'author', 'meta', 'thumb', 'content', 'modified_on', 'created_on', 'views', 'comments_count', 'comments']
    
    def get_author(self, obj):
        return obj.author.username
    
    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()