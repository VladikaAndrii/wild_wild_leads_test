from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.CharField(verbose_name='Position', max_length=164, blank=True, null=True)


class Order(models.Model):
    task_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Description")
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, verbose_name="Empoloyee")
