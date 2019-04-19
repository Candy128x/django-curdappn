from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=16)
    ename = models.CharField(max_length=64)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=16)
    class Meta:
        db_table = "employee"