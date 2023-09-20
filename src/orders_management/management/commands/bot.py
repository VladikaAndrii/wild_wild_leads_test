import telebot
from django.core.management.base import BaseCommand
from telebot.types import Message
from django.conf import settings

from orders_management.management.commands.utils import get_task_message
from orders_management.models import TelegramUser, Employee

bot = telebot.TeleBot(settings.TELEGRAM_API_KEY)


@bot.message_handler(commands=['start', ])
def send_welcome(message: Message) -> None:
    telegram_user_id = message.from_user.id
    telegram_user_object_exist = TelegramUser.objects.filter(telegram_user_id=telegram_user_id).exists()
    if not telegram_user_object_exist:
        TelegramUser.objects.create(telegram_user_id=telegram_user_id)
        bot.reply_to(message, "Тепер я зможу відправляти тобі повідомлення про усі виконані замовлення")
    else:
        bot.reply_to(message, "Ви уже будете отримувати повідомлення про усі виконані замовлення")


def send_message_to_telegram(message_data: dict, employee: Employee) -> None:
    telegram_chat = TelegramUser.objects.first()
    if telegram_chat:
        message = get_task_message(message_data, employee)
        bot.send_message(telegram_chat.telegram_user_id, message)


class Command(BaseCommand):
    help = "Run the bot"

    def handle(self, *args, **options):
        bot.infinity_polling()
