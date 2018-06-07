from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myadmin.utils import table_filter, table_sort, table_search
# Create your views here.
from myadmin import king_admin
from crm import models
from king_admin.forms import create_model_form, CustomerModelForm
# Create your views here.
from . import serializers
from rest_framework.renderers import JSONRenderer


def index(request):
    return render(request, 'myadmin/index.html')


@csrf_exempt
def table_index(request):
    return render(request, "myadmin/table_index.html", {'table_list': king_admin.enabled_admins})


@csrf_exempt
def display_table_objs(request, app_name, table_name):
    if request.method == 'GET':
        admin_class = king_admin.enabled_admins[app_name][table_name]
        app_label = admin_class.model._meta.app_label
        table_verbose_name = admin_class.model._meta.verbose_name
        return render(request, "myadmin/table_objs.html", {
            "admin_class": admin_class,
            "app_name": app_name,
            'table_verbose_name': table_verbose_name,
            'table_name': table_name

        })
    if request.method == 'POST':
        admin_class = king_admin.enabled_admins[app_name][table_name]

        list_per_page = request.POST.get('rows')
        object_list = table_filter(request, admin_class)
        object_list = table_search(request, admin_class, object_list)

        paginator = Paginator(object_list, list_per_page)
        total = paginator.count
        page = request.POST.get('page')
        try:
            query_sets = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            query_sets = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            query_sets = paginator.page(paginator.num_pages)

        serializer = serializers.create_serializ_model(admin_class)(query_sets, many=True)
        return JsonResponse({"rows": serializer.data,
                             "total": total
                             }, safe=False)


def table_obj_change(request, app_name, table_name, obj_id):
    admin_class = king_admin.enabled_admins[app_name][table_name]
    model_form_class = create_model_form(request, admin_class)
    obj = admin_class.model.objects.get(id=obj_id)

    if request.method == "POST":
        form_obj = model_form_class(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return JsonResponse({
                'success':"success"
            })
    else:
        form_obj = model_form_class(instance=obj)
        for field in form_obj:
            print(dir(field.field))
        return render(request, "myadmin/table_obj_change.html", {"form_obj": form_obj,
                                                                 "admin_class": admin_class,
                                                                 "app_name": app_name,
                                                                 "table_name": table_name,
                                                                 "obj_id": obj_id
                                                                 })


def table_obj_add(request, app_name, table_name):
    admin_class = king_admin.enabled_admins[app_name][table_name]
    admin_class.is_add_form = True
    model_form_class = create_model_form(request, admin_class)

    if request.method == "POST":
        form_obj = model_form_class(request.POST)  #
        if form_obj.is_valid():
            form_obj.save()
            return redirect(request.path.replace("/add/", "/"))
    else:
        form_obj = model_form_class()