from django.urls import path 

from .views import AvalicaoGetPostAPIView, AvalicaoUpdatDeletAPIView, CursoGetPostAPIView, CursoUpdatDeletAPIView

urlpatterns = [
  path('cursos/', CursoGetPostAPIView.as_view(),name='cursosgetpost'),
  path('cursos/<int:pk>', CursoUpdatDeletAPIView.as_view(),name='cursosupdatdelet'),
  path('avaliacoes/', AvalicaoGetPostAPIView.as_view(), name='avaliacoesgetoist'),
  path('avaliacoes/<int:pk>', AvalicaoUpdatDeletAPIView.as_view(), name='avaliacoesupdatdelet'),
]