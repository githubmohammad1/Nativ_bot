from rest_framework import serializers, status
from .models import Answer,Question,Conversation
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'id','username', 'password','email')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'email': { 'required': True}}
        

         

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer']





        
class ConversationSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.question')
    answer = serializers.CharField(source='answer.answer')

    class Meta:
        model = Conversation
        fields = ['question', 'answer']
        



# class ConversationSerializer(serializers.ModelSerializer):
#     question = QuestionSerializer(read_only=True)
#     answer = AnswerSerializer(read_only=True)

#     class Meta:
#         model = Conversation
#         fields = [
#           #  'chat_id',
#             'question', 'answer']
