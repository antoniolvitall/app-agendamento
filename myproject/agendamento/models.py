from django.db import models


class Profissional(models.Model):
    nome = models.CharField(max_length=200)
    nome_social = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    data = models.DateField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

    def __str__(self):
        return f'Consulta com {self.profissional.nome} em {self.data}'