from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# -------------------------
# Conversation ViewSet
# -------------------------

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        """
        Create new conversation with list of participant IDs
        """
        participant_ids = request.data.get("participants", [])

        if not participant_ids:
            return Response({"error": "Participants required"}, status=400)

        conversation = Conversation.objects.create()
        conversation.participants.set(User.objects.filter(user_id__in=participant_ids))
        conversation.save()

        return Response(ConversationSerializer(conversation).data, status=201)


# -------------------------
# Message ViewSet
# -------------------------

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        sender_id = request.data.get("sender")
        conversation_id = request.data.get("conversation")
        message_body = request.data.get("message_body")

        sender = User.objects.get(user_id=sender_id)
        conversation = Conversation.objects.get(conversation_id=conversation_id)

        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )

        return Response(MessageSerializer(message).data, status=201)
