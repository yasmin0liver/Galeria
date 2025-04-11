from django.contrib import admin
from django.urls import path
from JurassicDataBase import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('sobre/', views.sobre)  # Adicionei a barra final para consistência
]
