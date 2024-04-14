from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=32)
    def __str__(self):
        return self.question
    


class Anser(models.Model):
    anser = models.CharField(max_length=32)
    def __str__(self):
        
        return self.anser
    
    
class Conversation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anser=models.ForeignKey(Anser, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.anser    