from django.urls import path
from . import views 

urlpatterns = [
    path('auth/login', views.LoginView.as_view(), name='user_login'),
    path('auth/register', views.SignupView.as_view(), name='signup'),
    path('questions', views.QuestionsView.as_view(), name='all_questions'),
    path('questions/<str:questionID>', views.get_or_delete_QuestionsView.as_view(), name='selected_question'),
    path('questions/<str:questionID>/answers', views.SendAnswersView.as_view(), name='post_answer'),
    path('questions/<str:questionID>/answers/<str:answerID>', views.update_answers_view, name='update_answer'),
    path('logout/', views.LogoutUserView.as_view(), name='user_logout'),
    

]