from django.urls import path
from . import views

urlpatterns = [
    path('', views.turmas, name='turmas'),
    path('home/<int:id>/', views.home, name='home')
]