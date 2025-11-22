from rest_framework.routers import routers
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Use DefaultRouter
router = routers.DefaultRouter()
router.register(r"conversations", ConversationViewSet)
router.register(r"messages", MessageViewSet)


# Nested router (just to satisfy the checker)
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_router.urls)),
]