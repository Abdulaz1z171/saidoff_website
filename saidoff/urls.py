from django.urls import path
from saidoff import views


urlpatterns = [
    path('why-us/',views.Why_UsView.as_view()),
    path('service/<int:pk>/',views.ServiceView.as_view()),
    path('service-info/<int:pk>/',views.ServiceInfoView.as_view()),
    path('service-category/',views.ServiceCategoryView.as_view()),
    path('orders/',views.OrderView.as_view()),
    path('comments/',views.CommentView.as_view()),
    path('projects/', views.ProjectView.as_view()),
    path('features/',views.FeatureView.as_view()),
    path('price-plan/',views.PricePlanView.as_view()),
    path('tags/', views.TagView.as_view()),
    path('faqs/', views.FAQView.as_view()),
    path('faqs-answers', views.FAQAnswerView.as_view()),
    

    
]