from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid 
# Create your models here.



class Categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

#Models for Cases
class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class License(models.Model):
    TYPE =[
        ("POR","Ported"),
        ("GEN","GENERIC"),
        ("INT","International")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    type = models.CharField(max_length=5, choices=TYPE, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


class Case(models.Model):

    #Foreign KEy to User Model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    case_id = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    modified_date = models.DateTimeField(default=timezone.now)
    
    contribution_credit = models.NullBooleanField()
    consent = models.BooleanField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    language = models.CharField(max_length=50, null=True, blank=True)
    cc_license = models.ForeignKey(License, null=True, blank=True, on_delete=models.PROTECT)
    
    jurisdiction = models.CharField(max_length=500, null=True, blank=True, help_text="Within Country")
    court_name = models.CharField(max_length=500, help_text="Original and/or English Translation")
    decision_place = models.CharField(max_length=500, null=True, blank=True)
    decision_date = models.DateTimeField(null=True, blank=True) 

    background_info = models.TextField(max_length=5000, null=True, blank=True)
    summary_decesion = models.TextField(max_length=5000, null=True, blank=True)
    result_ruling = models.TextField(max_length=5000, null=True, blank=True)
    implication = models.TextField(max_length=5000, null=True, blank=True)
    categories = models.ManyToManyField(Categories)
    
    file = models.FileField(upload_to='case_files',null=True)
    
    published = models.BooleanField(default=True)
    notes = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

class LinkCase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    type = models.CharField(max_length=100, null=True, blank=True)
    case = models.ForeignKey(Case, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.type} {self.url}'

#Scholarship Data Models
class Scholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CharField)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    modified_date = models.DateTimeField(default=timezone.now)
    contribution_credit = models.NullBooleanField()
    consent = models.BooleanField()
    country = models.ForeignKey(Country , on_delete=models.PROTECT)
    title = models.CharField(max_length=500)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    date_published = models.DateTimeField()
    abstract = models.TextField(max_length=5000)
    summary = models.TextField(max_length=5000, null=True, blank=True)
    category = models.ManyToManyField(Categories)
    file = models.FileField(upload_to='scholarship_files',null=True)
    published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.title}'

class LinkScholarship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    type = models.CharField(max_length=100, null=True, blank=True)
    case = models.ForeignKey(Scholarship, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.type} {self.url}'
    