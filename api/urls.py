from django.urls import path
from . import views 

urlpatterns = [
    path('questions', views.get_all_questions_view, name='all_questions'),
    path('questions/<str:questionID>', views.get_selected_question_view, name='selected_question'),

]