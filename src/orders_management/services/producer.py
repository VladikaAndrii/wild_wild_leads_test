from random import choice, randint
from orders_management.models import Employee, Order


class Producer:
    def __init__(self):
        self.employee = None
        self.task_id = None

    def create_order(self) -> None:
        self.employee = self._get_random_employee()
        orders_count = self._get_count_orders()
        self.task_id = self._generate_task_id()
        self._create_order(orders_count)

    def _create_order(self, orders_count) -> None:
        name = f'Order №{orders_count + 1}'
        description = f'ID: {self.task_id}'

        Order.objects.create(
            task_id=self.task_id,
            name=name,
            description=description,
            employee=self.employee
        )

    @staticmethod
    def _get_count_orders() -> int:
        return Order.objects.count()

    @staticmethod
    def _get_random_employee() -> Employee:
        employees = Employee.objects.filter(is_superuser=False)
        return choice(employees)

    @staticmethod
    def _generate_task_id() -> int:
        return randint(100000, 999999)
