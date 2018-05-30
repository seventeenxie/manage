
from django.conf.urls import url
from myadmin import views

urlpatterns = [
    url(r'^$', views.index,name="myadmin/index"),
    url(r'table_index', views.table_index, name="table_index"),
]
