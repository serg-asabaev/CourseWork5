from django.db import models

from config.settings import AUTH_USER_MODEL

class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )

    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.CharField(max_length=100, verbose_name="Время")
    action = models.CharField(max_length=100, verbose_name="Действие")

    is_pleasure_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')

    linked_habit_1 = models.ForeignKey(
            'self',
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            related_name='linked_habit'
        )

    period = models.PositiveIntegerField(default=0, verbose_name="Периодичность", help_text="в днях")
    award = models.CharField(max_length=100, blank=True, null=True, verbose_name="Вознаграждение")

    time_to_execution = models.PositiveIntegerField(default=0, verbose_name="Время на выполнение")

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    class Meta:
        ordering = ['id']


class LinkedHabit(models.Model):
    parent_habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Привычка",
        related_name="parent",
    )

    child_habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Связанная привычка",
        related_name="child",
    )