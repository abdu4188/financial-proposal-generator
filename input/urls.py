from django.urls import path
from . import views

urlpatterns = [
    path('', views.InputPage.as_view(), name='input'),
    path('result/', views.ResultPage.as_view(), name='result')
]
