from django.db import models

# Create company models here.
class Company(models.Model):
    comapny_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
    ('non IT','non IT'),
    ('phone','phone')
    ))
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

# create employee models here 

class Employee(models.Model):
    Company=models.ForeignKey(Company, related_name='Employee', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(('manager','mg'),
    ('softwere developer','sd'),
    ('project','pj')
    ))


