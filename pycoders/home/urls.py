from django.contrib import admin
from django.urls import path
from .views import *


app_name='home'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('show/', ListHome.as_view()),
    path('',home,name='home'),
    path('<int:id>', get_recommendations, name='recommended'),
    path('search/', searchbar, name='search'),
    path('update/', update_data, name='shop'),
    # path('sprod/', sprod, name='sprod'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('update_data/',update_data)

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
