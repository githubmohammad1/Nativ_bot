from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

from rest_framework.authtoken.views import  * #obtain_auth_token

router = routers.DefaultRouter()

router.register('question', QuestionViewSet)#           تستخد للإظهار قائمة بالرسائبل السابقة  
router.register('users__register', UsersRegister)#                   تسجيل مستخدم جديد


urlpatterns = [
    path('', include(router.urls)),
    path('add',addquestion),#                               معالجة السؤال
    path("test",test_flutterapp),
    path("login",login),#                          تسسسسسسسسسسسسسسسسجيييييييييييييلل الدخوووووووووووول
    path("replic",run_model),
    path('re',return_conversation),
    path('adconv',add_question_and_answer),
path('aud',receiveaudio),
    
    

]
