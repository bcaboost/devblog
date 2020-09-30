from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.http import HttpResponse

from blogs.views import signup


def custom_page_not_found(request):
    return HttpResponse('PAGE NOT FOUND')



urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', LoginView.as_view(template_name='forms.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dev-admin/', admin.site.urls),
    path('api/post/', include('blogs.api.urls')),
    path('api/user/', include('blogs.user_api.urls')),
    path('api/', include('pages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blogs.urls')),
    path("404/", custom_page_not_found),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)