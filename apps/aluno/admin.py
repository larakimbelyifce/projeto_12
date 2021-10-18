from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
       list_display = ['nome', 'cpf', 'user']
       
admin.site.register(Aluno,AlunoAdmin)
