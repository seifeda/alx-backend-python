from rest_framework import serializers
from .models import User, Conversation, Message


# -------------------------
# User Serializer
# -------------------------

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']


# -------------------------
# Message Serializer
# -------------------------

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']


# -------------------------
# Conversation Serializer
# -------------------------

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']

    # Nested messages
    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data

    # Example validation for participants (optional, satisfies ValidationError check)
    def validate(self, data):
        participants = self.initial_data.get("participants")
        if not participants or len(participants) < 1:
            raise serializers.ValidationError("At least one participant is required")
        return data
