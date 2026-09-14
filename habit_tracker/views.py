from django.shortcuts import render
from rest_framework import generics, viewsets, filters

from .models import Habit

class HabitListAPIView(generics.ListAPIView):
    serializer_class = Habit
    queryset = Habit.objects.all()