from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import QuestionViewSet

router = routers.DefaultRouter()

router.register('question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
