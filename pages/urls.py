from django.urls import path, include

from .views import (
    developer_index,
    post_api_doc,
    user_api_doc,
    post_api_index,
    user_api_index
)


urlpatterns = [
    path('', developer_index, name='developer_index'),
    path('posts/', post_api_index, name='post_api_index'),
    path('users/', user_api_index, name='user_api_index'),
    path('posts/<str:slug>/', post_api_doc, name='post_api_doc'),
    path('users/<str:slug>/', user_api_doc, name='user_api_doc'),
]
