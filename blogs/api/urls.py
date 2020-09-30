from django.urls import path, include

from .views import (
    IndexPostAPI,
    CreatePostAPI,
    SinglePostAPI,
    UpdatePostAPI,
    DeletePostAPI,
    AuthorPostAPI,
    CommentPostAPI
)


urlpatterns = [
    path('', IndexPostAPI.as_view(), name='index_post_api'),
    path('author/<str:author>/', AuthorPostAPI.as_view(), name='author_post_api'),
    path('create/', CreatePostAPI.as_view(), name='create_post_api'),
    path('<str:slug>/', SinglePostAPI.as_view(), name='single_post_api'),
    path('<str:slug>/update/', UpdatePostAPI.as_view(), name='update_post_api'),
    path('<str:slug>/delete/', DeletePostAPI.as_view(), name='delete_post_api'),
    path('<str:slug>/comments/', CommentPostAPI.as_view(), name='comments_post_api'),
]
