from rest_framework import serializers
from .models import Avaliacao, Curso

class AvaliacaoSerializer(serializers.ModelSerializer):
  class Meta:
    # Configs extras
    extra_kargs = {
      'email': {'write_only' : True}
    }
    model = Avaliacao

    # Campos para apresentar do model
    fields = (
      'id',
      'curso',
      'nome',
      'email',
      'comentario',
      'avaliacao',
      'criacao',
      'ativo',
    )

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = (
      'id',
      'titulo',
      'url',
      'criacao',
      'ativo',
    )