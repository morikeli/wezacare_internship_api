from django.contrib import admin
from .models import Questions, Answers

@admin.register(Questions)
class QuestionsTable(admin.ModelAdmin):
    list_display = ['author', 'question', 'posted']

@admin.register(Answers)
class AnswersTable(admin.ModelAdmin):
    list_display = ['author', 'answer', 'posted']
    