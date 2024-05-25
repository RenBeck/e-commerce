from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.Marketing.as_view(), name="marketing"),
    path('produto/', views.ListaProdutos.as_view(), name="lista"),
    path('<slug:slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('adicionaraosacola/', views.AdicionarAosacola.as_view(),
         name="adicionaraosacola"),
    path('removerdosacola/', views.RemoverDosacola.as_view(),
         name="removerdosacola"),
    path('sacola/', views.sacola.as_view(), name="sacola"),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name="resumodacompra"),
    path('busca/', views.Busca.as_view(), name="busca"),
    path('busca/<str:categoria>', views.CategoriaBusca.as_view(), name="buscacategoria"),
    path('busca/<str:categoria>/<str:subcategoria>', views.SubCategoriaBusca.as_view(), name="buscasubcategoria"),
    path('busca/<str:categoria>/<str:subcategoria>/<str:tipo>', views.TipoBusca.as_view(), name="buscatipo"),
    path('outlet/', views.Outlet.as_view(), name="outlet"),
]
