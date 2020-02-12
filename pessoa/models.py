from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=100)
    idade = models.IntegerField("Idade")
    foto = models.ImageField('Foto', upload_to='imagens', null=True,
                             blank=True)

    def __str__(self):
        return self.nome
