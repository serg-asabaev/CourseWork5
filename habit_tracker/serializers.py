from rest_framework import serializers, viewsets

from habit_tracker.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"