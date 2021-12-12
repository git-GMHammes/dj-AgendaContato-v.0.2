from django.urls import path
from . import views

urlpatterns = [
    # -------- ↓ Arq view.py
    path('', views.index, name='index'),
    # def index():  ↑ do arq view.py
]
