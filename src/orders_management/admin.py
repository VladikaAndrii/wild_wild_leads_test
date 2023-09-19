from django.contrib import admin

# Register your models here.
from django.contrib import admin

from orders_management.models import Order, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'probation', 'position')


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'name', 'description', 'employee')
