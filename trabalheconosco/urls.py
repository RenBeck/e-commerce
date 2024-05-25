from django.urls import path
from . import views

app_name = 'trabalheconosco'

urlpatterns = [
    path('', views.ListaVagas.as_view(), name="listavagas"),
    path('curriculo/', views.Curriculo.as_view(), name="curriculo")
]
