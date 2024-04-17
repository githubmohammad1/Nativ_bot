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
from .gradio import *
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@api_view(['GET','POST'])

def addquestion(request):
    
    if request.method=='GET':
        output = query({
	"inputs": "teel me a story ",
                  })
        print(output)
        # print(type(output))
        # # Convert the output to a string
        # output_string = str(output)
        # print(output_string[24:-1])
        # serializer=AnserSerializer(data=output_string)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
# Store the string in a list
        

# Now you can access the converted string in 'output_list'
        
        

        question=Question.objects.latest('id')
        serializer=QuestionSerializer(question)
        print(type(serializer.data))
        import json
        json_string = json.dumps(serializer.data)

# Now 'json_string' contains the serialized JSON representation of 'return_dict'
        print(json_string)
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
    
        
        
        
        
        
        
        
