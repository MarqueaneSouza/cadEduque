from django import forms
from django.forms import ModelForm
from cadastro.models import Professor

class FormProfessor(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control form-select'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),


        }
