"""
URL configuration for elibe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import RegisterView, UserMeView
from book.views import BookViewSet
from author.views import AuthorViewSet
from bookmark.views import BookmarkViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)
# router.register(r'mark', BookmarkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
        path('external-books/', include('external_books.urls')),
    path('api/', include(router.urls)),
    path('', include('bookmark.urls')),
    path('test/me/', UserMeView.as_view(), name='user-me'),
    path('auth/sign-up/', RegisterView.as_view(), name='sign-up'),
    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
