from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from orders_management.services.utils import create_employees


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.CharField(verbose_name='Position', max_length=164, blank=True, null=True)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"


class Order(models.Model):
    task_id = models.PositiveIntegerField(unique=True, verbose_name='Task id')
    name = models.CharField(max_length=100, verbose_name='Order name')
    description = models.TextField(verbose_name="Description")
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, verbose_name="Empoloyee")

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'ID: {self.task_id} Name: {self.name}'


class TelegramUser(models.Model):
    telegram_user_id = models.IntegerField(unique=True)


@receiver(post_migrate)
def initial_employees(sender, **kwargs) -> None:
    """
    If there`re less than 3 Employee, we fill it.
    """
    employee_count = Employee.objects.count()
    if employee_count < 3:
        create_employees(Employee, employee_count)
