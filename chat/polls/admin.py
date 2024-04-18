from django.contrib import admin

# Register your models here.
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    fields = ["question_text"]
admin.site.register(Question, QuestionAdmin)

