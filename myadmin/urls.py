
from django.conf.urls import url
from myadmin import views

urlpatterns = [
    url(r'^$', views.index,name="myadmin/index"),
    url(r'table_index', views.table_index, name="table_index"),
    url(r'^(\w+)/(\w+)/$', views.display_table_objs,name="table_objs"),
    url(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change, name="table_obj_change"),

]
