from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path('diagnose/', views.diagnosis, name = 'diagnosis'),
    path('diagnose/liver/', views.liver, name = 'liver'),
    path('diagnose/liver/report', views.lpredictor, name = 'lpredict'),
    path('diagnose/kidney/', views.kidney, name = 'kidney'),
    path('diagnose/kidney/report', views.kdpredictor, name = 'kidneyReport'),
    path('diagnose/heart/', views.heart, name = 'heart'),
    path('diagnose/heart/report', views.hdpredictor, name = 'heartReport'),
    path('diagnose/diabetes/', views.diabetes, name = 'diabetes'),
    path('diagnose/diabetes/report', views.dbpredictor, name = 'diabetesReport'),
    path('service/', views.service, name='service'),
]