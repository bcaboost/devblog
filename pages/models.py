from django.db import models

from ckeditor.fields import RichTextField


class APIPostDoc(models.Model):
    title = models.CharField(max_length=254)
    menu = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    serial = models.IntegerField()
    published = models.BooleanField(default=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class APIUserDoc(models.Model):
    title = models.CharField(max_length=254)
    menu = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    serial = models.IntegerField()
    published = models.BooleanField(default=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title