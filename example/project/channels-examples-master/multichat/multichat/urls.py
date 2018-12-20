from django.urls import path
from django.contrib import admin
# from django.contrib.auth.views import login, logout
from chat.views import index
from django.urls import path, include # new
 

urlpatterns = [
    path('<room_name>/', index),
    # path('accounts/login/', login),
    # path('accounts/logout/', logout),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
