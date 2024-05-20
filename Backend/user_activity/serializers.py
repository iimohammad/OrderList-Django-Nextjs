from rest_framework import serializers
from userauths.serializers import UserSerializer
from user_activity.models import UserActivity

class UserActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserActivity
        fields = ['user','work_field','brands_related','tags_related','categoried_related','company']