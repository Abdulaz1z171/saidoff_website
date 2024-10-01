from rest_framework import serializers
from .models import *


class  OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['full_name','phone_number','service','message']

class  ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title','service_category']

class  ServiceCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['title']

class  ServiceInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = ['image','description','service']


class  Why_UsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Why_Us
        fields = ['image','description','title']

class  CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['full_name','profession','message','image']



class  FeatureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['title','is_checked',]

class  PricePlanModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlan
        fields = ['title','price','limit_date','limit_user','feature']

class  TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class  ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','image','url','tag']

class  FAQModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['title']

class  FAQAnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQAnswer
        fields = ['question','answer','faq']


class  SertificateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificate
        fields = ['title','image','description']

class  CoworkerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coworker
        fields = ['full_name','image','profession']



