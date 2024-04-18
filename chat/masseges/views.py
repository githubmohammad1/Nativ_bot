from rest_framework import request, status, viewsets
from .models import Question,Anser,Conversation
from .serializers import QuestionSerializer ,UserSerializer,AnserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .gradio import *

class UsersViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    
    

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    


@api_view(['GET','POST'])

def addquestion(request):
    
    if request.method=='GET':
        output = str(query({"inputs": "teel me a story ",}))
        
   
        answer=Anser(anser=output)
        answer.save()
        print(answer.anser)
        
        all_anser=Anser.objects.all()
        print(all_anser)
        
                

        question=Question.objects.latest('id')
        serializer=QuestionSerializer(question)

        return Response(serializer.data)
    
    elif  request.method=='POST':
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            
            # serializer.save()
            
            question=Question(question=serializer.data)
            question.save()
            print(question.question)
 
            output=str(query({"inputs":str(serializer.data),}))
            answer=Anser(anser=output)
            answer.save()
            print(answer.anser)
            conver=Conversation(question=question,anser=answer,user=User.objects.get(pk=1)
)
            conver.save()
            print(conver.anser)
            # print(conver.question)
            
   
            
            return Response(serializer.data)
         
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
        
        
        
        
        
        
        
