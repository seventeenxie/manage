
from django.conf.urls import url
from myadmin import views

urlpatterns = [
    url(r'^$', views.index,name="table_index"),
]
