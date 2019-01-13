from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('input/', views.input_page, name='input_page'),
    path('login_user/', views.login_user, name='login_user'),
]
