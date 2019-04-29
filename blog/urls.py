from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = "blog"

urlpatterns=[
    path('', views.post_list, name = 'post_list'),
    path('createChar/', views.createChar, name='createChar'),
    path('charDetails/<int:pk>/', views.charDetails, name='charDetails'),
    path('createResposta/<int:pk>/', views.createResposta, name='createResposta'),
    path('createRespostaResposta/<int:pkPost>/<int:pkResposta>/', views.createRespostaResposta, name='createRespostaResposta'),
    path('post/', views.postCreate, name='postCreate'),
    path('postRead/<int:pk>/', views.readPost, name='postRead'),
    path('postCat/<str:categoria>', views.post_listCategoria, name='postCat'),
    path('charList/', views.charList, name='charList'),
    path('createAventura/', views.createAventura, name='createAventura'),
    path('aventuras_list/', views.aventuras_list, name='aventuras_list'),
	path('aventura_details/<int:pk>', views.aventura_details, name='aventura_details'),
    # url(r'quiz/', views.quizList, name='quizList')
    

    



]
