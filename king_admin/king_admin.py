#__author:  Administrator
#date:  2017/1/5

from crm import models


enabled_admins = {}

class BaseAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 1
    ordering = None
    filter_horizontal = []
    actions = ["delete_selected_objs"]
    readonly_fields = []

class CustomerAdmin(BaseAdmin):
    list_display = ["id",'qq','name','source','consultant','consult_course','date','status']
    list_filters = ['source','consultant','consult_course','status','date']
    search_fields = ['qq','name',"consultant__name"]
    filter_horizontal = ('tags',)
	

    #model = models.Customer
    list_per_page = 1
    ordering = "qq"



    actions = ["delete_selected_objs","test"]
    def test(self,request,querysets):
        print("in test",)
    test.display_name  = "测试动作"

class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ('customer','consultant','date')


def register(model_class,admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {} #enabled_admins['crm'] = {}
    #admin_obj = admin_class()
    admin_class.model = model_class #绑定model 对象和admin 类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    #enabled_admins['crm']['customerfollowup'] = CustomerFollowUpAdmin


register(models.Customer,CustomerAdmin)
register(models.CustomerFollowUp,CustomerFollowUpAdmin)



