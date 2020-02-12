from django.forms import ModelForm
from pessoa.models import Pessoa


class PessoasForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'foto']
