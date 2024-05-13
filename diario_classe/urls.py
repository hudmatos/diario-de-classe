from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('turmas/', include('turmas.urls')),
    path('home/', include('turmas.urls')),
    path('chamada/<int:id>/', include('chamada.urls')),
    path('notas/<int:id>/', include('notas.urls')),
    path('programados/<int:id>/', include('programados.urls')),
    path('ocorrencias/<int:id>/', include('ocorrencias.urls')),
]
