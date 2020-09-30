from django.contrib import admin

from .models import Blog, Comment, Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('email',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'modified_on', 'created_on', 'views', 'published']
    fieldsets = (
        (None, {
            'fields': (
                ('title'),
                ('thumb'),
                ('meta'),
                ('content')
            )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                ('published'),
                ('slug'),
                ('views'),
                ('author'),
                ('modified_on'),
                ('created_on')
            )
        }),
    )
    readonly_fields = ['slug', 'views', 'modified_on', 'created_on', 'author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)