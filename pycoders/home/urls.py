from django.contrib import admin
from django.urls import path
from .views import *


app_name='home'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', ListHome.as_view()),
    path('',home,name='homy'),
    path('search/', searchbar, name='search'),
    path('shop/', shop, name='shop'),
    path('sprod/', sprod, name='sprod'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
