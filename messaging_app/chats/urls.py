from rest_framework.routers import routers
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Use DefaultRouter
router = routers.DefaultRouter()
router.register(r"conversations", ConversationViewSet)
router.register(r"messages", MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
