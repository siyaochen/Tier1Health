from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_page, name='input_page'),
]
