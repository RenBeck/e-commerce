from django.urls import path
from . import views

app_name = 'nossaloja'

urlpatterns = [
    path('', views.ListaLojas.as_view(), name="listalojas"),
]
