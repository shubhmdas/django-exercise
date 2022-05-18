from rest_framework import serializers
from message.models import Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'message', 'created_at', 'updated_at', 'created_by']