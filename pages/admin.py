from django.contrib import admin

from .models import APIPostDoc, APIUserDoc


@admin.register(APIPostDoc)
class APIPostDocAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'modified_on', 'published')
    list_filter = ('published', 'modified_on')
    search_fields = ('title', 'slug')


@admin.register(APIUserDoc)
class APIUserDocDocAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'modified_on', 'published')
    list_filter = ('published', 'modified_on')
    search_fields = ('title', 'slug')