from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views import View


class DispatchLoginRequiredMixin(View):
    pass


class Pagar(DispatchLoginRequiredMixin, DetailView):
    pass


class SalvarSacola(View):
    pass


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    pass


class Lista(DispatchLoginRequiredMixin, ListView):
    pass

