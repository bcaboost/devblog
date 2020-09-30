from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from .serializers import (
    SignupSerializer,
    LoginSerializer,
    ProfileSerializer,
    ProfileListSerializer,
    PasswordSerializer
)
from .paginations import (
    PostLimitPagination,
    PageNumberPagination
)
from blogs.models import Blog


class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer


class LoginAPI(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProfileUpdateAPI(UpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *agrs, **kwargs):
        queryset_list = User.objects.filter(is_active=True)
        user = self.request.user
        queryset_list = queryset_list.filter(username=user)
        return queryset_list


class ProfileAPI(RetrieveAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *agrs, **kwargs):
        queryset_list = User.objects.filter(is_active=True)
        user = self.request.user
        queryset_list = queryset_list.filter(username=user)
        return queryset_list


class ProfileListAPI(ListAPIView):
    serializer_class = ProfileListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'created_on', 'views']
    pagination_class = PostLimitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *agrs, **kwargs):
        queryset_list = Blog.objects.filter(author=self.request.user).order_by('-created_on')
        return queryset_list


class PasswordAPIView(UpdateAPIView):
    serializer_class = PasswordSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *agrs, **kwargs):
        queryset_list = User.objects.filter(is_active=True)
        user = self.request.user
        queryset_list = queryset_list.filter(username=user)
        return queryset_list