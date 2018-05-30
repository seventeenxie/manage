from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from myadmin import king_admin
# Create your views here.
def index(request):
    return  render(request,'myadmin/index.html')
@csrf_exempt
def table_index(request):
    return render(request, "myadmin/table_index.html", {'table_list': king_admin.enabled_admins})
