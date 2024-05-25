from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from ..forms import CurriculoForm

class CurriculoForm_Test(TestCase):
    def test_perfilForm_valido(self):
        # Simulando um arquivo de upload
        arquivo_content = b'conteudo_do_arquivo'
        arquivo = SimpleUploadedFile('curriculo.pdf', arquivo_content)

        form = CurriculoForm(data={
            'nome': 'Jose', 
            'email': 'jose@gmail.com', 
            'vaga': 'GL',
        }, files={'arquivo': arquivo})
        self.assertTrue(form.is_valid())
