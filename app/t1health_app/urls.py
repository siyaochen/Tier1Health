from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('input/', views.input_page, name='input_page'),
    # path('', views.login_user, name='login_user'),
]
