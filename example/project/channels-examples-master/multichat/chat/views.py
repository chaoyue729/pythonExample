from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Room
import json

@login_required
def index(request, room_name):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    print('index room_name : ' + room_name)
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "index.html", {
        "rooms": rooms,
        "room_name": mark_safe(json.dumps(room_name))
    })
