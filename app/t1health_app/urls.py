from django.urls import path, include
from . import views
from t1health_app.views import favicon_view

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('input/', views.input_page, name='input_page'),
    path('send_message/', views.send_messagefunc, name='send_messagefunc'),
    path('favicon.ico', favicon_view),
    # path('', views.login_user, name='login_user'),
]