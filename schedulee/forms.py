from .models import Agendamento
from django import forms

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data_hora', 'descricao', 'titulo']