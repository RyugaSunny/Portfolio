from django.urls import path
from listodo import views

urlpatterns = [
    path('todo/', views.index),
]
