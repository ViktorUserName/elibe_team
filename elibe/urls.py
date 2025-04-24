from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from bookmark.views import BookmarkViewSet
from genres.views import GenreViewSet
from user.views import RegisterView, UserMeView
from book.views import BookViewSet
from author.views import AuthorViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # ++++++++++AUTH++++++++++
    path('test/me/', UserMeView.as_view(), name='user-me'),
    path('auth/sign-up/', RegisterView.as_view(), name='sign-up'),
    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ++++EXTERNAL LIBS++++
    path('external-books/', include('external_books.urls')),
]
