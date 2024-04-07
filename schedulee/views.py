from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .models import Agendamento
from .forms import ScheduleForm


def bahia(request): 
    return HttpResponse('Tá perdido amigão a bahia fica pra lá>>>>>>>')

    
def criar_agendamento(request):
    if request.method == 'POST':
        form = ScheduleForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else: 
        form = ScheduleForm()
    return render(request, 'criar_agendamento.html', {'form':form})

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamentos':agendamentos})