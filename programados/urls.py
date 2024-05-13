from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.programados, name='programados'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete')
]