from datetime import datetime

from orders_management.models import Employee


def get_task_message(message_data: dict, employee: Employee) -> str:
    pk = message_data.get('pk')
    task_id = message_data.get('task_id')
    name = message_data.get('name')
    employee_info = f'{employee.first_name} - {employee.position}'
    time = datetime.now()

    message = (
        f'Задача №{pk}-{task_id} під назвою: {name}\n'
        f'була опрацьована {employee_info} об {time} 🟢'
    )
    return message
