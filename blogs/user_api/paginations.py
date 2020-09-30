from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class PostLimitPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50


class PostPagePagination(PageNumberPagination):
    page_size = 10