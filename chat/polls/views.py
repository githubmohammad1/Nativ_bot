from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404

from polls.models import  Question 
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.serializers import QuestionSerializer
from rest_framework import status
from django.template import loader
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token


import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from django.urls import reverse

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@api_view()
def view_dtl(request):
      return Response({'success':409,'message':'api'})

      

@api_view(['GET','POST'])
def view_question(request):

      
    
      if request.method=='GET':
            authentication_classes = [TokenAuthentication]
            permission_classes = [IsAuthenticated]
           
            q=Question.objects.all()
            serializer=QuestionSerializer(q,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      elif request.method=='POST':

            serializer=QuestionSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  
                  #return Response({'msg':'question adding','data':serializer.data},status=status.HTTP_201_CREATED)
                  return Response(serializer.data)
            
            
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      else:
            return Response({'msg':'invalid request'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
                  

def index(request):
      
      
           
      q=Question.objects.all()
      serializer=QuestionSerializer(q,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

      





def addquestion(request,test_text):
      q = Question(test_text=request.GET(),
                   pub_date=timezone.now())
      q.save()
      return HttpResponse(q.question_text)

def predict(request,test_number):
      i=1
      if i==1:
            import numpy as np
            print('load tensorflow ffffffff')
      
            from tensorflow import keras
            model = keras.models.load_model('./models/model.h5')
            i=0
      
            
      r=np.array(test_number)
      r=np.array([r],dtype=float)
   
      
      r=model.predict(r)
          
      return HttpResponse("predict is  %s." % r)
 
      
      
      
