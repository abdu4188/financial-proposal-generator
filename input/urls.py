from django.urls import path
from . import views

urlpatterns = [
    path('', views.inputPage, name='home'),
    path('result/', views.resultPage, name='result')
]
