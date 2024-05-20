from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from userauths.models import User, Profile
from userauths.serializers import (
    MyTokenObtainPairSerializer, 
    RegisterSerializer,
    UserSerializer,
    ProfileSerializer,
    verifyPhoneSerializers,
)
from django.shortcuts import get_object_or_404
from django.conf import settings
import random
from kavenegar import *
from kavenegar import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


def generate_otp_sms():
    otp = ''.join(random.choices('0123456789', k=6))
    return otp


class Phone_Verification_send_sms(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get_object(self):
        user = self.request.user
        

        if user and user.is_verify_phone==False:
            user.otp = generate_otp_sms()
            user.save()
            message = f"سلام کد تایید شما {user.otp} می باشد."
            self.send_sms(user.phone, message)

        return user

    def send_sms(self, receivers, message):
        api_key = settings.KAVENEGAR_API_KEY
        try:
            api = KavenegarAPI(api_key)
            params = {
                'sender': '10006926',
                'receptor': str(receivers),
                'message': message,
            } 
            response = api.sms_send(params)
            print(response)
        except APIException as e: 
            print(e)
        except HTTPException as e: 
            print(e)


class Phone_Verification(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = verifyPhoneSerializers

    def get_object(self):
        user = self.request.user
        return user
    
    def post(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.otp == serializer.validated_data.get('otp'):
            user.is_verify_phone = True
            user.save()

            return Response(serializer.data)
        else:
            return Response({'detail': 'Invalid OTP or unauthorized user.'}, status=status.HTTP_400_BAD_REQUEST)


 
class ProfileViewSet(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=request.user.id)
        serializer = ProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


        

