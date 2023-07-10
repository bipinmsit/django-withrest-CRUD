from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=60)
    emp_sal = models.IntegerField()
    emp_id = models.IntegerField()
    emp_addr = models.CharField(max_length=100)
