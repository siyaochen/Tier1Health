from django.urls import path, include
from . import views
from t1health_app.views import favicon_view

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('input/', views.statisticinput, name='statisticinput'),
    path('inputed/', views.statistic_new, name='statistic_new'),
    path('send_messagefunc_weight/', views.send_messagefunc_weight, name='send_messagefunc_weight'),
    path('send_messagefunc_bmi/', views.send_messagefunc_bmi, name='send_messagefunc_bmi'),
    path('send_messagefunc_nutrition/', views.send_messagefunc_nutrition, name='send_messagefunc_nutrition'),
    path('send_messagefunc_exercise/', views.send_messagefunc_exercise, name='send_messagefunc_exercise'),

    path('favicon.ico', favicon_view),
    path('fitness_page/', views.fitness_page, name="fitness_page"),
    path('nutrition_page/', views.nutrition_page, name="nutrition_page"),
    path('results_weight_page/', views.results_weight_page, name="results_weight_page"),
    path('results_bmi_page/', views.results_bmi_page, name="results_bmi_page"),
    path('results_nutrition_page/', views.results_nutrition_page, name="results_nutrition_page"),
    path('results_exercise_page/', views.results_exercise_page, name="results_exercise_page"),

]