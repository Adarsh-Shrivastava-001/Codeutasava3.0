from django.contrib import admin
from django.urls import path
from .views import *


app_name='dataanalysis'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('cluster/', user_cluster, name='search'),
	path('time/', time_graph, name='time'),    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
