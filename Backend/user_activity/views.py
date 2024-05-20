from rest_framework import generics, status, permissions
from user_activity.serializers import UserActivitySerializer
from user_activity.models import UserActivity

class UserActivityCreateView(generics.CreateAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserActivitySerializer
    
    def get_queryset(self):
        user = self.request.user
        query = UserActivity.objects.filter(user = user)
        return query


class UserActivityCreateView(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserActivitySerializer
    queryset = UserActivity.objects.all()