from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UsersViewSet,
                    get_token, send_confirmation_code)

urlpatterns = [
    path(
        'v1/auth/token/',
        get_token,
        name='get_token'
    ),
    path(
        'v1/auth/signup/',
        send_confirmation_code,
        name='send_confirmation_code'
    ),
]

router_v1 = DefaultRouter()

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review',
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register('users', UsersViewSet, basename='users')

urlpatterns += [
    path('v1/', include(router_v1.urls)),
]
