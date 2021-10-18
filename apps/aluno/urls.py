from django.urls import path, include
from django.contrib import admin
from apps.core import views
from . import views

app_name = 'aluno'

# Chamar a view.
#    urlpatterns = [
#        path('', views.AddAluno, name='add_aluno'),
#        path('lista/', views.lista_alunos, name='lista_alunos'),
#    ]

urlpatterns = [
    # Add a view do core
    path('',views.HomeView.as_view(),name='home'),
    path('novo/',views.AddAluno,name='add_aluno'),
    path('lista/',views.ListAlunosView.as_view(),name='lista_alunos'),
    path('editar/<int:id_aluno>/',views.edit_aluno,name='edit_aluno'),
    path('delete/<int:id_aluno>/',views.deleteAluno,name='delete_aluno'),
]
