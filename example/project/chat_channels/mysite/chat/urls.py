from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
	path('', views.index, name='index'),
	path('send/', views.send, name='send'),
    # url('^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('<slug:room_name>', views.room, name='room'),
]
