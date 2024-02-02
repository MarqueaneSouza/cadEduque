from django import forms
from django.forms import ModelForm
from cadastro.models import Professor

class FormProfessor(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
