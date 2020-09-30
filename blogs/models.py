from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from ckeditor.fields import RichTextField
import readtime

from .customs import unique_slug

class Blog(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(unique=True, editable=False)
    meta = models.TextField()
    thumb = models.URLField(null=True, blank=True, help_text='We do not support uploading files.', verbose_name='Thumbnail URL')
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, editable=False)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(Blog, self.title)
        return super(Blog, self).save(*args, **kwargs)

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text


class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextField(config_name='comment_editor')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment on {} by {}'.format(self.post, self.name)


class Subscriber(models.Model):
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email