from rest_framework import serializers, status
from .models import Anser,Question,Conversation

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'id','username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        
 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anser
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'