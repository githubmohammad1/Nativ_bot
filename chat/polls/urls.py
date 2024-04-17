from django. urls import path
from polls.views import *
from . import views
app_name = "polls"

urlpatterns=[
path("index",views.index,name="index"),
           

#path("<int:question_id>/results/", views.results, name="results"),



path("predict/<int:test_number>/", views.predict, name="predict"),


path("add_question/<str:test_text>", views.addquestion, name="addquestion"),

path('',view_dtl,name='dtl'),


path('view/',view_question,name='question'),

]
