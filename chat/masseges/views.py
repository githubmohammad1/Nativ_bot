from rest_framework import request, status, viewsets
from .models import Question,Anser
from .serializers import QuestionSerializer ,UserSerializer,AnserSerializer

from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@api_view(['GET','POST'])

def addquestion(request):
    
    if request.method=='GET':
        question=Question.objects.latest('id')
        serializer=QuestionSerializer(question)
        return Response(serializer.data)
    elif  request.method=='POST':
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a=Anser()
            a.anser=request.data['anser']
            a.save()
            
            print(a.anser)
            
            return Response(serializer.data)
         
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
        
        
        
        
        
        
        
