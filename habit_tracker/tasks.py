from celery import shared_task

from habit_tracker.services import send_telegram_message

@shared_task
def habit_reminder(habit_id):
    # send_telegram_message("")
    pass