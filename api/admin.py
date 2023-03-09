from django.contrib import admin
from .models import Questions, Answers, User

@admin.register(User)
class UsersTable(admin.ModelAdmin):
    list_display = ['username', 'email']
    readonly_fields = ['password']

@admin.register(Questions)
class QuestionsTable(admin.ModelAdmin):
    list_display = ['author', 'question', 'posted']

@admin.register(Answers)
class AnswersTable(admin.ModelAdmin):
    list_display = ['author', 'answer', 'posted']
    