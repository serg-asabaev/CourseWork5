from celery import shared_task
from datetime import date, datetime
from django.utils import timezone


from habit_tracker.services import send_telegram_message
from users.models import User
from habit_tracker.models import Habit

@shared_task
def habit_reminder():
    """ Отправка напоминаний в телеграм-бот о привычках """

    habits_list = Habit.objects.all()

    for habit in habits_list:

        today = timezone.now()
        last_remind = habit.last_remind

        if last_remind is None:
            last_remind = today

        date_diff = today - last_remind

        if date_diff.days < habit.period and habit.last_remind is not None:
            continue

        if not habit.is_pleasure_habit:
            useful = "полезной"
        else:
            useful = "приятной"

        message = f"Сегодня вам нужно {habit.action} {habit.time} в {habit.place} в качестве {useful} привычки!"

        if habit.user is None:
            continue

        tg_chat_id = habit.user.tg_chat_id

        if tg_chat_id:
            send_telegram_message(tg_chat_id, message)
            habit.last_remind = timezone.now()
            habit.save()