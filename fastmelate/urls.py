from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('salir/', views.salir, name='salir'),
    path('panel/', views.panel, name='panel'),
    path('generar_numero/', views.generar_numero, name='generar_numero'),
    path('ver_numeros/', views.ver_numeros, name='ver_numeros'),
    path('eliminar_numero/<int:id>/', views.eliminar_numero, name='eliminar_numero'),
]
