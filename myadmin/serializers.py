from rest_framework import serializers
from crm import models

def create_serializ_model(admin_class):

  class Meta:
        model = admin_class.model
        fields =admin_class.list_display




  attr={'Meta':Meta,
        }

  serialize_model=type('Dynamic_serizlize_model',(serializers.ModelSerializer,), attr)

  return serialize_model


class CustomerSerializer(serializers.ModelSerializer):
    operate = serializers.SerializerMethodField()
    class Meta:
        model = models.Customer
        fields = ('id','operate')
    def get_operate(self, obj):
        return 'fffff'
