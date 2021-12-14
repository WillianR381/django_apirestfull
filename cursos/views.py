from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import AvaliacaoSerializer, CursoSerializer

# Lista todos os cursos ou/e Cria um novo curso
class CursosGetPostAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 

class CursosUpdatDeletAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 


class AvaliacoesGetPostAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        print(self.lookup_field)
        if self.kwargs.get('curso_pk'):
          return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacoesUpdatDeletAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer