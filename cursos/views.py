from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import AvaliacaoSerializer, CursoSerializer

# Lista todos os cursos ou/e Cria um novo curso
class CursoGetPostAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 

class CursoUpdatDeletAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 


class AvalicaoGetPostAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvalicaoUpdatDeletAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer