import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    events = []
    events.append({
        'category': 'Eventos',
        'nome': 'Brasil Game Show 2023',
        'date_time': '11 a 15 de Outubro',
        'description': 'Evento ocorre no Expo Center Norte, em São Paulo'
    })
    events.append({
        'category': 'Eventos',
        'nome': 'CCXP 2023',
        'date_time': '30 de novembro a 3 de dezembro',
        'description': 'São Paulo Expo - Rodovia dos Imigrantes, em São Paulo'
    })
    context = {
        'title': "Summer Sale chegou na Steam!",
        'text': "Obtenha todos os nossos grandes jogos! E se você já tem alguns deles... sem problemas. O Steam carrega apenas os jogos que não estão na sua biblioteca!",
        'date_time': datetime.datetime.now(),
        'categories': ['Lançamentos', 'Jogos em Promoção', 'Eventos'],
        'events': events
    }
    return render(request, 'index.html', context)
