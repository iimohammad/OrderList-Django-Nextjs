from rest_framework import generics, permissions
from supportsite.serializers import MessageForSupportSerializer, AnswerSerializer
from supportsite.models import MessageForSupport

class SendMessageToTechnicalSupport(generics.CreateAPIView):
    permission_classes= [permissions.AllowAny]
    serializer_class = MessageForSupportSerializer()
    def get_queryset(self):
        user= self.request.user
        user_message = MessageForSupport.objects.filter(sender=user)
        return user_message
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
         

class ShowAllReceiveMessages(generics.ListAPIView,generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class= AnswerSerializer()

    queryset = MessageForSupport.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class ShowUserReceiveMessages(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class= AnswerSerializer()

    def get_queryset(self):
        user = self.request.user
        queryset = MessageForSupport.objects.filter(receiver=user)
        return queryset


