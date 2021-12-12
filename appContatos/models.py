from django.db import models
# ↓ Acrescentar esta importação:
from django.utils import timezone
# → Importei por causa do campo ↓
# → models.DateTimeField(default=timezone.now)


# → Antes de tudo executar o comando
# → python manage.py migrate

# Create your models here.


class DbTabCategoria(models.Model):
    strNome = models.CharField(max_length=255)
# ATENÇÃO: Esta classe deve vir primeiro
# MOTIVO: Para ser referenciada pela classe abaixo

    def __str__(self) -> str:
        return self.strNome


class DbTabContatos(models.Model):
    strNome = models.CharField(max_length=255)
    strSobreNome = models.CharField(max_length=255, blank=True)
    strTelefone = models.CharField(max_length=255, blank=True)
    strEmail = models.CharField(max_length=255, blank=True)
    strDataCriacao = models.DateTimeField(default=timezone.now)
    # ↑ Utilizei a importação: ↑ from django.utils import timezone
    texDescricao = models.TextField(blank=True)
    strKeyTabCategoria = models.ForeignKey(
        DbTabCategoria, on_delete=models.DO_NOTHING)
    # ↑ Referencia class DbTabCategoria(models.Model):

    def __str__(self) -> str:
        return self.strNome

    # Depois de concluir ou alterar etse arquivo faça:
    # Execute os comandos:
    # python manage.py makemigrations
    # python manage.py migrate
#
# Após a criação do models, ir para a área administrativa:
# admin.py
