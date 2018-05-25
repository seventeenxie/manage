from django.test import TestCase

from crm import  models



class Test(TestCase):
   def setUp(self):
        print("start")

   def testTime(self):
     queryset=models.Customer.objects.filter(id=1)
     print(queryset)


   def tearDown(self):
        print("======in tearDown")