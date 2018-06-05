from rest_framework import serializers
from crm import models

def create_serializ_model(admin_class):
  class Meta:
        model = admin_class.model
        fields = admin_class.list_display
  attr={'Meta':Meta}
  serialize_model=type('Dynamic_serizlize_model',(serializers.ModelSerializer,), attr)
  return serialize_model
