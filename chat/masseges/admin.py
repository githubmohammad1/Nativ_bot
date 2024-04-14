from django.contrib import admin
from .models import Question,Anser,Conversation
# Register your models here.
admin.site.register(Question)
admin.site.register(Anser)
admin.site.register(Conversation)