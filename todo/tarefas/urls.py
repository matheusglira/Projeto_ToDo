from django.urls import path

from . import views

app_name = 'tarefas_url'

urlpatterns = [
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('delete-categoria/(?P<id>[0-9]+)', views.delete_categoria, name='delete_categoria'),
    path('editar-categoria/(?P<id>[0-9]+)', views.editar_categoria, name='editar_categoria'),
    path('nova-tarefa/', views.nova_tarefa, name='nova_tarefa'),
    path('delete-tarefa/(?P<id>[0-9]+)', views.delete_tarefa, name='delete_tarefa'),
    path('editar-tarefa/(?P<id>[0-9]+)', views.editar_tarefa, name='editar_tarefa'),

]
