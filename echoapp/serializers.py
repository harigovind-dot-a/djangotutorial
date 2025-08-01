from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['created_at']

class EchoInputSerializer(serializers.Serializer):
    message = serializers.CharField()
