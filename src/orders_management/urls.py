from django.urls import path

from orders_management.views import TablePageView, DeleteTaskView

app_name = "orders_management"

urlpatterns = [
    path('', TablePageView.as_view(), name='main-page'),

    path('api/delete-task/<int:task_id>', DeleteTaskView.as_view(), name='delete-task')
]
