

from modeltranslation.translator import TranslationOptions, translator
from .models import *


class OrderTranslationOptions(TranslationOptions):
    fields = ('message',)  # Specify the fields to be translated

class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title',)

class ServiceInfoTranslationOptions(TranslationOptions):
    fields = ('description',)

class Why_UsTranslationOptions(TranslationOptions):
    fields = ('title','description')

class OrderTranslationOptions(TranslationOptions):
    fields = ('message',)

class CommentTranslationOptions(TranslationOptions):
    fields = ('profession', 'message')


class PricePlanTranslationOptions(TranslationOptions):
    fields = ('title','limit_date','limit_user')


class FeatureTranslationOptions(TranslationOptions):
    fields = ('title',)

class TagTranslationOptions(TranslationOptions):
    fields = ('title',)

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title',)

class FAQTranslationOptions(TranslationOptions):
    fields = ('title',)


class FAQAnswerTranslationOptions(TranslationOptions):
    fields = ('question','answer')

class CoworkerTranslationOptions(TranslationOptions):
    fields = ('profession',)

class SertificateTranslationOptions(TranslationOptions):
    fields = ('title','description')

for i,j in [(Order,OrderTranslationOptions),(ServiceCategory,ServiceCategoryTranslationOptions),(Service,ServiceTranslationOptions),(Why_Us,Why_UsTranslationOptions),(Comment,CommentTranslationOptions),(PricePlan,PricePlanTranslationOptions),(Tag,TagTranslationOptions),(Project,ProjectTranslationOptions),(Sertificate,SertificateTranslationOptions),(Coworker,CoworkerTranslationOptions),(FAQ,FAQTranslationOptions),(FAQAnswer,FAQAnswerTranslationOptions),(Feature,FeatureTranslationOptions)]:
    translator.register(i,j)
