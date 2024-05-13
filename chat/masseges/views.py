from rest_framework import request, status, viewsets
from .models import *
from .serializers import *
from django.contrib.auth.models import User

from rest_framework.decorators import action, api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from .gradio import *

from django.core.exceptions import ObjectDoesNotExist

class UsersRegister(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        print(request.data)
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
@authentication_classes([TokenAuthentication])

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
    # token, created = Token.objects.get_or_create(user=User.objects.get(pk=1))
    return HttpResponse("wlkom to django servereeeeeeeeeeeeeeeeeeeeennnnnnnnnnnnnndddddddddddddddddddddddsspeeeeeeeeek")
# Response({
#             'token': token.key,
#         })


 



@api_view(['GET','POST'])
def login(request):
    username = request.data.get('username')
    email= request.data.get('email')
    try:
        user = User.objects.get(username=username,email =email)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({ 'token': token.key,})
    except User.DoesNotExist:
        return Response({'error': 'اسم المستخدم غير موجود'}, status=400)

        
        
        
        
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# from .models import YourModel  # قم بتعيين النموذج الخاص بك إذا كان لديك

# @csrf_exempt  # تعطيل التحقق من صحة رمز الحماية المشتركة (CSRF)
@api_view(['POST'])  # تحديد الطرق المقبولة للطلبات
def run_model(request):
    if request.method == 'POST':
        # استدعاء النموذج هنا واسترداد النتيجة
        # يمكنك استخدام chain_with_message_history.invoke() هنا لتشغيل النموذج
        
        # على سبيل المثال:
        output = chain_with_message_history.invoke(
            {"input": request.POST.get('input_text')},
            {"configurable": {"session_id": "001"}},
        )

        # تنسيق الاستجابة بشكل صحيح، عادةً ما يكون بتنسيق JSON
        response_data = {
            'output': output,
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})