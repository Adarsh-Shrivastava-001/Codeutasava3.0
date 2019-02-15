from django.contrib import admin
from django.urls import path
from .views import *


app_namne='home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', ListHome.as_view())
]