from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,HttpResponse
import importlib
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myadmin.utils import  table_filter,table_sort,table_search
# Create your views here.
from myadmin import king_admin
from crm import models
from king_admin.forms import create_model_form,CustomerModelForm
# Create your views here.
def index(request):
    return  render(request,'myadmin/index.html')
@csrf_exempt
def table_index(request):
    return render(request, "myadmin/table_index.html", {'table_list': king_admin.enabled_admins})
@csrf_exempt
def display_table_objs(request,app_name,table_name):
    admin_class = king_admin.enabled_admins[app_name][table_name]
    if request.method =='GET':
          return render(request, "myadmin/table_objs.html", {"admin_class": admin_class})
    if request.method == 'POST':
          query_set=admin_class.model.objects.all()
          print(query_set)



