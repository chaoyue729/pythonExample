from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from websocket import create_connection
import sys
import json

def send(request):
	raise ValueError
	return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	raise ValueError
	# try:
	# 	raise ValueError
	# except Exception as e:
	# 	# print(e)
	# 	print(sys.exc_info()[0])
	return render(request, 'chat/index.html', {})

def room(request, room_name):

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

