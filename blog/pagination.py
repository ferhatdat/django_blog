from rest_framework.pagination import (
    PageNumberPagination, 
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'sayfa'

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'ferhat'

class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'
    page_size = 8
    ordering = '-id'
