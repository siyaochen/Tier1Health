from django.urls import path, include
from . import views
from t1health_app.views import favicon_view

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('input/', views.input_page, name='input_page'),
    path('input2/', views.myFirstChart, name='myFirstChart'),
    path('send_message/', views.send_messagefunc, name='send_messagefunc'),
    path('favicon.ico', favicon_view),
    path('fitness_page/', views.fitness_page, name="fitness_page"),
    path('nutrition_page/', views.nutrition_page, name="nutrition_page"),
    path('results_page/', views.results_page, name="results_page"),
    # path('_page/', views.fitness_page, name="fitness_page"),

    # path('', views.login_user, name='login_user'),
]