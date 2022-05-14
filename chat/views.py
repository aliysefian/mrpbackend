from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import serializers

User = get_user_model()


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

