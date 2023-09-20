from django.urls import path

from orders_management.views import TablePage, DeleteTask

app_name = "orders_management"

urlpatterns = [
    path('', TablePage.as_view(), name='main-page'),

    path('api/delete-task/<int:task_id>', DeleteTask.as_view(), name='delete-task')
]
