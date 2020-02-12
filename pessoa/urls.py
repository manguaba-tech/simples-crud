from django.urls import path
from pessoa.views import listar, incluir, alterar, excluir

urlpatterns = [
    path('lista/',listar, name="listar" ),
    path('inclusao/', incluir, name="incluir"),
    path('alteracao/<int:id>/', alterar, name="alterar"),
    path('exclusao/<int:id>/', excluir, name="excluir"),
]
