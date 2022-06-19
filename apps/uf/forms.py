from django import forms
from uf.models import UF
from uf.validation import *


class UFForms(forms.ModelForm):
    class Meta:
        model = UF
        fields = '__all__'
        labels = {
            'uf_name': 'Nome',
            'uf_initials': 'Sigla'
        }
        
    def clean(self):
        uf_name = self.cleaned_data.get('uf_name')
        uf_initials = self.cleaned_data.get('uf_initials')
        lista_de_erros = {}
        #campo_tem_algum_numero(uf_name, 'uf_name', lista_de_erros)
        #campo_tem_algum_numero(uf_initials, 'uf_initials', lista_de_erros)
        if lista_de_erros is not None :
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data