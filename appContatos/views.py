from django.shortcuts import render

# Create your views here.


def index(request):
    # Aqui não é ponto (.) é barra ( / )
    # -------------------------------- ↓ -----------------
    return render(request, 'appContatos/contatoIndex.html')
# Pasta Templates past appContatos ↑   e     ↑ arquivo.html da past appContatos
