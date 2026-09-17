from rest_framework.serializers import ValidationError

from .models import Habit, LinkedHabit


class LinkedHabitAwardValidator:

    def __call__(self, award, linked_habit):
        if award is not None and linked_habit is not None:
            raise ValidationError("Связанная привычка и награда не могут быть заполнены одновременно!")