from django.db import models # type: ignore

class Agendamento(models.Model):
    data_hora = models.DateTimeField()
    descricao = models.TextField()
    titulo = models.CharField(max_length=50)
     