import datetime
from django.db import models
from django.utils import timezone
#Create your models here.

class Question(models.Model):
      
      
      question_text=models.CharField(max_length=200)
      # pub_date=models.DateTimeField("datepubliched")

            
      def __str__(self):
            
            return self.question_text

