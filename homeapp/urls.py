from django.urls import path
from homeapp import views

urlpatterns = [
    path('', views.index),
    path('oldindex/', views.oldindex, name='oldindex'),
    path('listodo/', views.todohome, name='todohome'),
    path('send_email/', views.send_email, name='send_email'),
]
