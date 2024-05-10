from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

from rest_framework.authtoken.views import  * #obtain_auth_token

router = routers.DefaultRouter()

router.register('question', QuestionViewSet)
router.register('users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add',addquestion),
    path("test",test_flutterapp)
    
    
    
]
