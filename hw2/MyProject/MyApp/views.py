from django.shortcuts import render
import logging
from .management.commands.create_client import Command_create
from .management.commands.get_client import Command_get
from .management.commands.update_client import Command_update
from .management.commands.delete_client import Command_delete
from random import choice
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page was requested.')
    return render(request, "index.html")

def create_clients(request):
    logger.info('Page of creating users was requested.')
    names = ['Alex', 'John', 'Lisa']
    emails = ['a@mail.ru', 'j@gmail.com', 'l@example.com']
    phones = ['789567', '89996721', '908667']
    addresses = ['Moscow', 'Saint Petersburg', 'Kazan']
    for _ in range(5):
        name = choice(names)
        email = choice(emails)
        phone = choice(phones)
        city = choice(addresses)
        command = Command_create()
        command.handle(name, email, phone, city)
    return HttpResponse('Five clients were created')

def get_client(request):
    logger.info('Get client by id page was requested.')
    command = Command_get()
    id = choice([1,2,3])
    client = command.handle(id)
    return HttpResponse(f'Client with id {id} is : {client}')

def get_all_client(request):
    logger.info('Get all clients page was requested.')
    clients = []
    command = Command_get()
    client = 0
    i = 1
    while client != None:
        client = command.handle(i)
        if client != None:
            clients.append(str(client))
        i += 1
    return HttpResponse(f'All clients are: {clients}')

def update_client_name(request):
    logger.info('Updating client page was requested.')
    command = Command_update()
    id = choice([1,2,3])
    name = choice(['George', 'Ron'])
    client = command.handle(id, name)
    return HttpResponse(f'Client {client} was updated')

def delete_client(request):
    logger.info('Deleting client page was requested.')
    command = Command_delete()
    id = choice([1,2,3])
    client = command.handle(id)
    return HttpResponse(f'Client {client} was deleted')