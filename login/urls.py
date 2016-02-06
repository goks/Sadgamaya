from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', views.auth, name='auth'),
    url(r'^dash/', views.dash, name='dash'),
    url(r'^tokenpass/',views.tokenpass, name='pass'),
    url(r'^chatbox/',views.chatbox, name='chatbox'),
    url(r'^chatcheck/',views.chatcheck, name='chatcheck'),
]
