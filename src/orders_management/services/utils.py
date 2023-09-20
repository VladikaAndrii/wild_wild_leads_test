from django.contrib.auth.hashers import make_password


def create_employees(instance, count: int) -> None:
    """ Creating 3 users """
    positions = {1: 'Developer', 2: 'QA', 3: 'HR'}

    for number in range(count + 1, 4):
        username = f'user_{number}'
        instance.objects.create(
            username=username,
            first_name=username,
            password=make_password('user_pass'),
            probation=True,
            position=positions.get(number)
        )
