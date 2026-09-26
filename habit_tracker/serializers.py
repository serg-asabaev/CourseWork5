from rest_framework import serializers, viewsets

from habit_tracker.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        award = data.get('award')
        linked_habit = data.get('linked_habit_1')
        is_pleasure_habit = data.get('is_pleasure_habit')
        period = data.get('period')
        time_to_execution = data.get("time_to_execution")

        if award and linked_habit:
            raise serializers.ValidationError({
                'award': 'Связанная привычка и награда не могут быть заполнены одновременно!',
                'linked_habit_1': 'Связанная привычка и награда не могут быть заполнены одновременно!'
            })

        if is_pleasure_habit and (linked_habit is not None or award is not None):
            raise serializers.ValidationError({
                'is_pleasure_habit': 'У приятной привычки не может быть вознаграждения или связанной привычки!',
            })

        if period > 7:
            raise serializers.ValidationError({
                'period': 'Нельзя выполнять привычку реже, чем 1 раз в 7 дней!',
            })

        if linked_habit is not None:
            if not linked_habit.is_pleasure_habit:
                raise serializers.ValidationError({
                    'linked_habit_1': 'В связанные привычки могут попадать только приятные привычки!',
                })

        if time_to_execution > 120:
            raise serializers.ValidationError({
                'time_to_execution': 'Время на выполнение не должно превышать 120 секунд!',
            })

        return data