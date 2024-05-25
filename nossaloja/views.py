from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Loja

class ListaLojas(ListView):
    model = Loja
    context_object_name = 'lojas'
    template_name = 'nossaloja/listalojas.html'
