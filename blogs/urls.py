from django.urls import path, include
from django.contrib.auth.views import PasswordChangeView

from .views import (
    homepage,
    single_post,
    author_page,
    create_post,
    update_post,
    delete_post,
    user_change,
    dashboard,
    subscribe
)


urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/create/', create_post, name='create_post'),
    path('dashboard/update/<str:slug>/', update_post, name='update_post'),
    path('dashboard/delete/', delete_post, name='delete_post'),
    path('dashboard/profile/', user_change, name='user_change'),
    path('dashboard/password/', PasswordChangeView.as_view(template_name='forms.html', success_url='/'), name='change_password'),
    path('subscribe/', subscribe, name='subscribe'),
    path('<str:author>/', author_page, name='author_page'),
    path('<str:author>/<str:slug>/', single_post, name='single_post'),
]
