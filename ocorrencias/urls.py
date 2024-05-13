from . import views
from django.urls import path

urlpatterns = [
    path('', views.ocorrencias, name="ocorrencias"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete")
]