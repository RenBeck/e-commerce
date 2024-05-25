from django import forms
from . import models


class CurriculoForm(forms.ModelForm):
    class Meta:
        model = models.Curriculo
        fields = ('nome', 'email', 'vaga', 'arquivo') 
        widgets = {
            'arquivo': forms.FileInput(attrs={'required': False})
        }
