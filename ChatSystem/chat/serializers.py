# serializers.py
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()



# urls.py
from django.urls import path
from .views import ChatAPIView

urlpatterns = [
    path('api/chat/<str:room_name>/', ChatAPIView.as_view(), name='chat-api'),
]
