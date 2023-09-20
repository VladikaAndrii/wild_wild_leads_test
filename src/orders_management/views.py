from typing import Any, Dict

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from orders_management.management.commands.bot import send_message_to_telegram
from orders_management.services.consumer import get_orders, delete_task


class TablePageView(LoginRequiredMixin, TemplateView):
    """
    Creating a table with user tasks.
    """

    template_name = 'orders_management/index.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_orders(employee=self.request.user)
        return context


class DeleteTaskView(View):
    """
    Delete task by his primary key and sending a message using Telegram bot.
    """

    success_url = reverse_lazy('orders_management:main-page')

    def post(self, request, task_id: int):
        employee = self.request.user

        message_data = delete_task(task_id=task_id)
        send_message_to_telegram(message_data=message_data, employee=employee)
        # send_message_to_telegram(message_data=message_data, employee=employee)

        return HttpResponseRedirect(self.success_url)
