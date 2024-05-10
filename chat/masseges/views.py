from rest_framework import request, status, viewsets
from .models import Question,Anser,Conversation
from .serializers import QuestionSerializer ,UserSerializer,AnserSerializer,ConversationSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.http import HttpResponse
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
        
        return Response("pleas make post rquest")
    
    elif  request.method=='POST':
        
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            
            # serializer.save()
            
            question=Question(question=serializer.data)
            question.save()
            
            # strr=serializer.data
            # print(strr)
            # strr=strr["question"]
            # print(strr)
            # output=my_client(strr)
            remasseg=str(question.question)
            # output=chatting(question.question)
            output=chatting(remasseg)
            # output=query({"inputs":serializer.data["question"],})
            # Assuming you want to use the first response
            
            

            
            answer=Anser(anser=output)
            
            answer.save()
            
            conver=Conversation(question=question,anser=answer,user=User.objects.get(pk=1))
            
            
            conver.save()
            
            
            # print(conver.question)
            
   
            
            return HttpResponse(conver.anser)#Response(r)
         
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
        
        
 


@api_view(['GET','POST'])
def test_flutterapp(request):
    queryset = Question.objects.all()
    return HttpResponse("wlkom to django servereeeeeeeeeeeeeeeeeeeeennnnnnnnnnnnnndddddddddddddddddddddddsspeeeeeeeeek")
            
        
        
        
        
