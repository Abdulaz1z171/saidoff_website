from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from .serializers import *

# Create your tests here.
# Testing for Why_Us model

class Why_UsTestCase(APITestCase):
    
    def setUp(self):
        self.why_us = Why_Us.objects.create(
            title='Test1',
            description= 'test1',
            image = 'test1.png'


        )
    
    def test_why_us(self):
        serializer = Why_UsModelSerializer(self.why_us)
        serializer_data = serializer.data

        self.assertEqual = (serializer_data['title'],'Test1')
        self.assertEqual = (serializer_data['description'],'test1')
        self.assertEqual = (serializer_data['image'],'/why_us/test1.png')

    def test_why_us_invalid_data(self):
    # Test if invalid data raises an error
        invalid_data = {'title': '', 'description': '','image': ''}
        serializer = Why_UsModelSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)


#   Testin for ServiceCategory, Service,ServiceInfo

class ServiceCategoryTestCase(APITestCase):

    def setUp(self):
        self.service_category = ServiceCategory.objects.create(
            title= 'test',
        )

        self.service = Service.objects.create(
            title= 'test',
            service_category= self.service_category,

        )

        self.service_info = ServiceInfo.objects.create(
            image = 'test.png',
            description= 'test',
            service= self.service

        )

        self.order = Order.objects.create(
            full_name='Aliyev Abdulaziz',
            phone_number='+998940212334',
            service=self.service,
            message = 'It is gonna be more fun!'
        )


    def test_service_category_section(self):

        serializer = ServiceCategoryModelSerializer(self.service_category)
        serializer_data = serializer.data

        self.assertEqual = (serializer_data['title'],'test')
    

    def test_service(self):
        serializer = ServiceModelSerializer(self.service)
        serializer_data = serializer.data

        self.assertEqual = (serializer_data['title'],'test')
        self.assertEqual = (serializer_data['service_category'],self.service_category.id)


#  Test for comment section

class CommentTestCase(APITestCase):
    def setUp(self):
        self.comment = Comment.objects.create(
            full_name= 'Jonny Deep',
            message = 'Hello everyone',
            profession = 'actor'
        )

    
    def test_comment(self):
        serializer = CommentModelSerializer(self.comment)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['full_name'],'Jonny Deep')
        self.assertEqual(serializer_data['message'],'Hello everyone')
        self.assertEqual(serializer_data['profession'],'actor')


class PricePlanTestCase(APITestCase):


    def setUp(self):
        self.feature = Feature.objects.create(
            title='Zor',
            is_checked=False
        )

    def setUp(self):
        self.price_plan = PricePlan.objects.create(
            title = 'Business',
            price = 120,
            limit_date= 'per month',
            limit_user = 'per user',
            features= self.feature

        )

    def feature_test(self):
        serializer = FeatureModelSerializer(self.feature)
        serializer_data = serializer.data
        self.assertEqual(serilizer_data['title'],'Zor')
        self.assertEqual(serializer_data['is_checked'],False)

    def price_plan_test(self):
        serializer = PricePlanModelSerializer(self.price_plan)
        serializer_data = serializer.data
        self.assertEqual = [serializer_data['title'],'Business']
        self.assertEqual = [serializer_data['price'],120]
        self.assertEqual = [serializer_data['limit_date'],'per_month']
        self.assertEqual = [serializer_data['limit_user'],'per month']
        self.assertEqual = [serializer_data['feature'],self.feature.id]