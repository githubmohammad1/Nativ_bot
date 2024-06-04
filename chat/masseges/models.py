from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    


class Answer(models.Model):
    answer = models.CharField(max_length=300)
    def __str__(self):
        
        return self.answer
    
    
class Conversation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE)
    chat_id=models.IntegerField(models.AutoField())
    
    
    # def __str__(self):
        
    #     return self.anser    