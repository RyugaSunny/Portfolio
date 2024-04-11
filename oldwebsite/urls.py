from django.urls import path
from oldwebsite import views

urlpatterns = [
    path('oldwebsite/', views.index),
]
