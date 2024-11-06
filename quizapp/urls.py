# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('quiz/<int:quiz_id>/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:quiz_id>/question/<int:question_index>/', views.start_quiz, name='quiz_question'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    # path('quiz/success/', views.quiz_success, name='quiz_success'),
    path('quiz/success/', views.quiz_success, name='quiz_success'),
   
]

