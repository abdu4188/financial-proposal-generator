from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.inputPage, name='home'),
    # path('result/', views.resultPage, name='result'),
    path('ajax/result/', views.resultPage, name='ajax'),
    path('login/', LoginView.as_view())
]
