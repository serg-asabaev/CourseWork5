from django.shortcuts import render
from rest_framework import generics, viewsets, filters

from habit_tracker.models import Habit
from .serializers import HabitSerializer

class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()