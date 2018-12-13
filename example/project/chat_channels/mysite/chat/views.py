from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from websocket import create_connection

import json

def send(request):
	# wsUrl = 'ws://118.218.215.211:8000/ws/chat/' + roomName + '/'
	wsUrl = 'ws://118.218.215.211:8000/ws/chat/1111-2222/'
	ws = create_connection(wsUrl)
	ws.send(json.dumps({'message': '99999999'}))
	ws.close()

	return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

