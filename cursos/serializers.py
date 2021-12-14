from rest_framework import serializers
from .models import Avaliacao, Curso

class AvaliacaoSerializers(serializers.ModelSerializer):
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

class CursoSerializers(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fiedls = (
      'id',
      'titulo',
      'url',
      'criacao',
      'ativo',
    )