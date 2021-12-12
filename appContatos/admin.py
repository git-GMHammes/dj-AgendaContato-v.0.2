from django.contrib import admin

# ↓ Criar usuário para área de admin
# → python manage.py createsuperuser
# → Usuário: djAdmin
# → E-mail: mail@habilidade.com
# → Senha: ************
# Register your models here.

# Perceba que será importado ↓ ------- ↓ Class
from .models import DbTabCategoria, DbTabContatos
# Este ↑ .models é o \djAgPy\appContatos\models.py

# Para realizar alterações ↓ na admin do django
class AdminContatos(admin.ModelAdmin):
    # ↓ O que será exibido no admin do django ↓ (Campos)
    list_display = ('id', 'strNome', 'strSobreNome', 'strEmail', 'strTelefone')
    # Campos da Tabela: 
    # → strNome, 
    # → strSobreNome, 
    # → strEmail, 
    # → strTelefone, 
    # → strDataCriacao, 
    # → texDescricao,
    # → strKeyTabCategoria. 
    #
    # ↓ Para que os campos virem hiperlinks ↓
    list_display_links = ('id', 'strNome', 'strSobreNome')
    # ↓ Para gerar filter no campo para area admin
    list_filter = ('strKeyTabCategoria',)
    # ↓ Paginação de N registros na lista admin
    list_per_page = 10
    # ↓ Gerar um campo de busca no admin
    search_fields = ('strNome', 'strSobreNome', 'strTelefone')
    
#
# NÃO deve conter [" "] aqui ↓
admin.site.register(DbTabCategoria)
# A AdminContato() instanciada aqui --- ↓
admin.site.register(DbTabContatos, AdminContatos)
