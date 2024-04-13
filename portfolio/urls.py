from django.urls import path
from portfolio import views

urlpatterns = [
    path('portfolio/', views.index),
    path('oldindex/', views.oldindex, name='oldindex'),
    path('listodo/', views.todohome, name='todohome'),
]
