from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookmarkViewSet

router = DefaultRouter()
router.register(r'bookmark', BookmarkViewSet)
urlpatterns = [
    path('', include(router.urls)),
]