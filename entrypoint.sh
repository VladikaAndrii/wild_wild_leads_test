#!/bin/sh


echo "The postgres host  is: $POSTGRES_HOST $POSTGRES_DB_PORT"
# Wait for the DB to be ready
until nc -z -v -w30 $POSTGRES_HOST $(( $POSTGRES_DB_PORT ));
do
 echo 'Waiting for the DB to be ready...'
 sleep 2
done

python manage.py makemigrations
python manage.py migrate

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
Employee = get_user_model()
if not Employee.objects.filter(username='admin').exists():
    user = Employee.objects.create_superuser(username='admin', password='admin')
EOF
python manage.py bot & python manage.py runserver 0.0.0.0:8000