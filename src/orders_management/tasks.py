from celery import shared_task

from orders_management.services.producer import ProducerService


@shared_task()
def create_order_task() -> None:
    ProducerService().create_order()
