from rest_framework import serializers
from userauths.serializers import UserSerializer
from .models import MessageForSupport
from userauths.models import User


class MessageForSupportSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_staff=True)
    )

    class Meta:
        model = MessageForSupport
        fields = ['sender', 'receiver', 'subject', 'message', 'attachment']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['sender'] = user

        if 'receiver' not in validated_data:
            admin_user = User.objects.filter(is_staff=True).first()
            if admin_user:
                validated_data['receiver'] = admin_user
            else:
                raise serializers.ValidationError("No admin user found")

        return super().create(validated_data)

class AnswerSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = MessageForSupport
        fields = ['sender', 'receiver', 'subject', 'message', 'attachment']