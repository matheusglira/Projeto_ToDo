from django import forms
from .models import Categoria, Tarefa

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite a categoria'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descreva a categoria...'}),
        }
        fields = '__all__'


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite a tarefa'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descreva a tarefa...'}),
            'data_final': forms.TextInput(attrs={'placeholder': '00/00/0000'})
        }
        fields = '__all__'
