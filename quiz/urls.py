from django.urls import path
from . import views

app_name = "quiz"

urlpatterns=[
   
   path('', views.quizList, name = 'quizList'),
   path('createQuiz/', views.CreateQuiz, name = 'CreateQuiz'),
   path('criarPerguntas/', views.CreatePerguntas, name = 'criarPerguntas'),
   path('fazerQuiz/<int:pkQuiz>', views.fazerQuiz, name = 'fazerQuiz'),
   path('pontuacao/', views.mostrarPontos, name='pontuacao'),

   
    



]
