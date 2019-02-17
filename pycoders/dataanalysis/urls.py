from django.contrib import admin
from django.urls import path
from .views import *


app_name='dataanalysis'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('', dashboard, name='dashboard'),
    path('cluster/', user_cluster, name='search'),
	path('time/', time_graph, name='time'),
	path('third_party', third_party, name='third_cluster')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
