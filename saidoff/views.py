from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.

from .models import *
from .serializers import *


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (AllowAny,)


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'pk'

    


class ServiceCategoryView(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategoryModelSerializer
    permission_classes = (AllowAny,)

class ServiceInfoView(generics.ListAPIView):
    queryset = ServiceInfo.objects.all()
    serializer_class = ServiceInfoModelSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'pk'
    

class Why_UsView(generics.ListAPIView):
    queryset = Why_Us.objects.all()
    serializer_class = Why_UsModelSerializer
    permission_classes = (AllowAny,)


class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = (AllowAny,)   

    
# class CommentApiView(ApiView)




class FeatureView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureModelSerializer
    permission_classes = (AllowAny,)  

class PricePlanView(generics.ListAPIView):
    queryset = PricePlan.objects.all()
    serializer_class = PricePlanModelSerializer
    permission_classes = (AllowAny,)   
 

class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    permission_classes = (AllowAny,) 


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    permission_classes = (AllowAny,)

class FAQView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQModelSerializer
    permission_classes = (AllowAny,)


class FAQAnswerView(generics.ListAPIView):
    queryset = FAQAnswer.objects.all()
    serializer_class = FAQAnswerModelSerializer
    permission_classes = (AllowAny,)

class CoworkerView(generics.ListAPIView):
    queryset = Coworker.objects.all()
    serializer_class = CoworkerModelSerializer
    permission_classes = (AllowAny,)

class Sertificateiew(generics.ListAPIView):
    queryset = Sertificate.objects.all()
    serializer_class = SertificateModelSerializer
    permission_classes = (AllowAny,)


class ServiceInfoView(generics.ListAPIView):
    queryset = ServiceInfo.objects.all()
    serializer_class = ServiceInfoModelSerializer
    permission_classes = (AllowAny,)
