from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models
from .forms import CurriculoForm
from django.contrib import messages

class ListaVagas(ListView):
    model = models.Vaga
    template_name = 'trabalheconosco/listavagas.html'
    context_object_name = 'vagas'

class Curriculo(View):
    template_name = 'trabalheconosco/form_curriculo.html'
    fields = ['nome', 'email', 'vaga', 'arquivo']

    def get(self, request, *args, **kwargs):
        form = CurriculoForm()
        return render(request, self.template_name, {'CurriculoForm': CurriculoForm})
    
    def post(self, request, *args, **kwargs):
        form = CurriculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curriculo enviado com sucesso')
    
        return render(request, self.template_name, {'CurriculoForm': CurriculoForm})