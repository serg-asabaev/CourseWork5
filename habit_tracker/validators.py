from rest_framework.serializers import ValidationError

from .models import Habit, LinkedHabit


# class LinkedHabitAwardValidator:
#
#     def __init__(self, award, linked_habit):
#         self.award = award
#         self.linked_habit = linked_habit
#
#     def __call__(self, award, linked_habit_1):
#         if award is not None and linked_habit_1 is not None:
#             raise ValidationError("Связанная привычка и награда не могут быть заполнены одновременно!")
