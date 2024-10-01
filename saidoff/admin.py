from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class OrderTranslationAdmin(TranslationAdmin):
    list_display = ('message',)

admin.site.register(Order, OrderTranslationAdmin)

class Why_UsTranslationAdmin(TranslationAdmin):
    list_display = ('title', 'description')

admin.site.register(Why_Us, Why_UsTranslationAdmin)

class CommentTranslationAdmin(TranslationAdmin):
    list_display = ('full_name',)

admin.site.register(Comment,CommentTranslationAdmin)

for a in [Partner, FAQ, FAQAnswer, Coworker,PricePlan,Feature,Service,ServiceCategory,ServiceInfo,Tag,Project]:
    admin.site.register(a)