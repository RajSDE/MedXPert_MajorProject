from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path('diagnose/', views.diagnosis, name = 'diagnosis'),
    path('diagnose/liver/', views.liver, name = 'liver'),
    path('diagnose/liver/report', views.lpredictor, name = 'lpredict'),
    path('service/', views.service, name='service'),
]