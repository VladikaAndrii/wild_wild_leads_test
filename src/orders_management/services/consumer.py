from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from orders_management.models import Order


def get_orders(employee) -> QuerySet[Order]:
    return Order.objects.filter(employee=employee)


def delete_task(task_id: int) -> dict:
    instance = get_object_or_404(Order, pk=task_id)
    result = {
        'pk': instance.pk,
        'task_id': instance.task_id,
        'name': instance.name
    }

    instance.delete()

    return result
