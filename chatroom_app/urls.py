from django.urls import path

from . import views


app_name = 'chatroom_app'
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('user', views.user, name='user'),
    path('do_login', views.do_login, name='do_login'),
    path('goregister', views.userRegister, name='goregister'),
    path('registersuc', views.registersuc, name='registersuccess'),
    path('websocket', views.websocket, name='websocket'),
    path('chatroom', views.chatroom, name='chatroom'),
    path('online_people', views.online_people, name='online_people'),

]