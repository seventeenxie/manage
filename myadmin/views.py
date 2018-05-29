from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request,'myadmin/index.html')
def table_index(request):
    return render(request,'myadmin/table_index.html')