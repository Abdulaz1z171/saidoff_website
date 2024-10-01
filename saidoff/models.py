from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class ServiceCategory(models.Model):
    title = models.CharField(max_length=255)
   
     
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    service_category = models.ForeignKey(ServiceCategory, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title


class ServiceInfo(models.Model):
    image = models.ImageField(upload_to = 'services')
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete= models.CASCADE)

class Why_Us(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'why_us')

    def __str__(self):
        return self.title

class Order(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    service = models.ForeignKey(Service,on_delete = models.CASCADE)
    message = models.TextField() 

    def __str__(self):
        return self.full_name  

class Comment(BaseModel):
    full_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to = 'comments',null=True, blank=True)
    
    def __str__(self):
        return self.full_name


class Feature(models.Model):
    title = models.CharField(max_length=255)
    is_checked = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title


class PricePlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    limit_date = models.CharField(max_length=255)
    limit_user = models.CharField(max_length=255)
    feature = models.ManyToManyField(Feature)
    





class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Project(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'projects')
    url = models.URLField()
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class FAQAnswer(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    faq = models.ForeignKey(FAQ, on_delete= models.CASCADE)





class Coworker(models.Model):
    full_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'coworkers')

    def __str__(self):
        return self.full_name

class Partner(models.Model):
    image = models.ImageField(upload_to = 'partners')

    class Meta:
        verbose_name = 'Partner'


class Sertificate(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'sertificates')

    def __str__(self):
        return self.title
