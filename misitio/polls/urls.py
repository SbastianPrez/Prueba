from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ex:/encuestas/2/
    path('<int:id_pregunta>/', views.detalle, name='detalle'),



    #ex: /Encuestas/agregar_respuestas
    path('agregar_preguntas/', views.agregar_preguntas, name='agregar_preguntas'),

    #ex: /Encuestas/Validar_Formulario
    path('Validar_Formulario/', views.Validar_Formulario, name='Validar_Formulario')