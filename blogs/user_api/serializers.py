from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from blogs.models import Blog, Comment


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password2 = serializers.CharField(label='Confirm Password', write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        obj = User(first_name=first_name, last_name=last_name, email=email, username=username)
        obj.set_password(password)
        obj.save()
        return validated_data
    
    def validate_username(self, value):
        banned = ['self', 'api', 'login', 'logout', 'register', 'dashboard', 'about', 'contact', 'dev-admin', 'ckeditor']
        if value in banned:
            raise serializers.ValidationError('You cannot use this username.')
        return value
    
    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get('password')
        password2 = value
        if password != password2:
            raise serializers.ValidationError('Password fields do not match.')
        return value


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = { 'password': {'write_only': True}}
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if not username:
            raise serializers.ValidationError('Username is required to login.')
        try:
            user = User.objects.get(username=username)
            res = user.check_password(password)
            if res:
                token, created = Token.objects.get_or_create(user=user)
                data['token'] = token.key
            else:
                raise serializers.ValidationError('Login credientials do not match')
        except:
            raise serializers.ValidationError('Login credientials do not match')
        return data


class ProfileListSerializer(serializers.ModelSerializer):
    full_post = serializers.HyperlinkedIdentityField(view_name='single_post_api', lookup_field='slug')
    comments_count = serializers.SerializerMethodField(method_name='get_comments_count')
    comments = serializers.HyperlinkedIdentityField(view_name='comments_post_api', lookup_field='slug')
    update = serializers.HyperlinkedIdentityField(view_name='update_post_api', lookup_field='slug')
    delete = serializers.HyperlinkedIdentityField(view_name='delete_post_api', lookup_field='slug')

    class Meta:
        model = Blog
        fields = ['title', 'meta', 'thumb', 'created_on',  'views', 'comments_count', 'comments', 'full_post', 'update', 'delete']

    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()


class PasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True)
    new_password2 = serializers.CharField(write_only=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'password', 'new_password', 'new_password2']
        extra_kwargs = {'password': {'write_only': True, 'label': 'Old Password'}}

    def update(self, instance, validated_data):
        username = validated_data.get('username', instance.username)
        password = validated_data['password']
        new_password2 = validated_data['new_password2']
        try:
            obj = User.objects.get(username=username)
            res = obj.check_password(password)
            if res:
                obj.set_password(new_password2)
                obj.save()
            else:
                raise serializers.ValidationError('Login credientials do not match')
        except:
            raise serializers.ValidationError('Login credientials do not match')
        return validated_data

    def validate_new_password2(self, value):
        data = self.get_initial()
        new_password = data.get('new_password')
        new_password2 = value
        if new_password != new_password2:
            raise serializers.ValidationError('Password fields do not match.')
        return value