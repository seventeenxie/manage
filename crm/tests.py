from django.test import TestCase
from django.forms import ModelForm
# Create your tests here.

from crm import models
class Test(TestCase):
    def setUp(self):
        print("======in setUp")

    def test(self):
     objs=models.Customer.objects.all()
     for obj in objs:
       print(obj.name)


     def tearDown(self):
        print("======in tearDown")