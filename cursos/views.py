from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao

from .serializers import AvaliacaoSerializers, CursoSerializers




class CursoAPIView(APIView):

  def get(self,request):
    cursos = Curso.objects.all()
    serializer = CursoSerializers(cursos, many=True)
    return Response(serializer.data)


class AvalicaoAPIView(APIView):

  def get(self, request):
    avaliacoes = Avaliacao.objects.all()
    serializer = AvaliacaoSerializers(avaliacoes, many=True)
    return Response(serializer.data)