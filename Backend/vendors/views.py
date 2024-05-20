from django.shortcuts import render
from vendors.serializers import ResponseOrdersSerializer
from vendors.models import ResponseOrders
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db import IntegrityError


class ResponseOrdersView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ResponseOrdersSerializer()
    queryset = ResponseOrders.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            message = "Response Order have to be unique"
            return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)


class ResponseOrdersListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ResponseOrdersSerializer()
    queryset = ResponseOrders.objects.all()