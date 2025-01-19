# flake8: noqa
from datetime import datetime, timedelta

from celery import shared_task

import users
from habits.models import Habit
from habits.services import send_telegram

from .models import Habit





from datetime import datetime, timedelta
from .models import Habit

@shared_task
def send_reminder():
    """Отправляет напоминания пользователям о привычках в назначенное время."""

    now = datetime.now()
    time_threshold = now - timedelta(seconds=40)

    # Фильтруем привычки, которые нужно напомнить
    habits_to_remind = Habit.objects.filter(time_for_habit__lte=now.time(), time_for_habit__gte=time_threshold.time())

    for habit in habits_to_remind:
        chat_id = habit.user.tg_chat_id
        if chat_id:
            message = f'Я буду {habit.action} в {habit.time_for_habit} в {habit.place}'
            send_telegram(chat_id, message)
            print('Сообщение отправлено')
