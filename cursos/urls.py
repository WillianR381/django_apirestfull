from django.urls import path 

from .views import CursosGetPostAPIView,CursosUpdatDeletAPIView,AvaliacoesGetPostAPIView, AvaliacoesUpdatDeletAPIView

urlpatterns = [
  path('cursos/', CursosGetPostAPIView.as_view(),name='cursosgetpost'),
  path('cursos/<int:pk>', CursosUpdatDeletAPIView.as_view(),name='cursosupdatdelet'),
  path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesGetPostAPIView.as_view(),name='cursos_avaliacaogetpost'),
  path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacoesUpdatDeletAPIView.as_view(),name='cursos_avaliacaoupdatdelet'),
  
  path('avaliacoes/', AvaliacoesGetPostAPIView.as_view(), name='avaliacoesgetpost'),
  path('avaliacoes/<int:avaliacao_pk>', AvaliacoesUpdatDeletAPIView.as_view(), name='avaliacoesupdatdelet'),
]