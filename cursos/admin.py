from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'url', 'criacao','atualizacao','ativo')


@admin.register(models.Avaliacao)
class AvalicaoAdmin(admin.ModelAdmin):
  list_display = ('curso','nome','email','avaliacao','criacao','atualizacao','ativo')
  