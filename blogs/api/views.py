from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

from .permissions import IsOwner
from .paginations import (
    PostLimitPagination,
    PageNumberPagination
)
from blogs.models import Blog, Comment
from .serializers import (
    PostListSerializer,
    PostReadSerializer,
    PostCreateUpdateSerializer,
    CommentSerializer,
    CommentPostSerializer
)


class IndexPostAPI(ListAPIView):
    queryset = Blog.objects.filter(published=True).order_by('-created_on')
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'created_on', 'views']
    pagination_class = PostLimitPagination

    # def get_queryset(self, *agrs, **kwargs):
    #     queryset_list = Blog.objects.filter(published=True)
    #     query = self.request.GET.get('q')
    #     if query:
    #         queryset_list = queryset_list.filter(title__icontains=query)
    #     return queryset_list


class CreatePostAPI(CreateAPIView):
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SinglePostAPI(RetrieveAPIView):
    queryset = Blog.objects.filter(published=True)
    serializer_class = PostReadSerializer
    lookup_field = 'slug'


class AuthorPostAPI(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'created_on', 'views']
    pagination_class = PostLimitPagination

    def get_queryset(self, *agrs, **kwargs):
        queryset_list = Blog.objects.filter(published=True).filter(author__username=self.kwargs['author']).order_by('-created_on')
        return queryset_list


class UpdatePostAPI(RetrieveUpdateAPIView):
    queryset = Blog.objects.filter(published=True)
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsOwner]


class DeletePostAPI(DestroyAPIView):
    queryset = Blog.objects.filter(published=True)
    serializer_class = PostListSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsOwner]


class CommentPostAPI(ListAPIView):
    serializer_class = CommentPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *agrs, **kwargs):
        queryset_list = Comment.objects.filter(active=True, post__slug=self.kwargs['slug'], post__author=self.request.user).order_by('-created_on')
        return queryset_list