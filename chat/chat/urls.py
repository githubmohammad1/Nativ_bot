from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from masseges import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('masseges.urls')),
    path('tokenrequest/', obtain_auth_token),
    path("add/",views.addquestion)
]
