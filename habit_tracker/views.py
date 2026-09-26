from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import transaction
from django.db.models import Q

from habit_tracker.models import Habit
from .serializers import HabitSerializer
from habit_tracker.pagination import HabitPagination
from habit_tracker.permissions import IsEmptyOwner, IsOwner, IsPublic


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     queryset = Habit.objects.all()
    #     paginated_queryset = self.paginate_queryset(queryset)
    #     serializer = HabitSerializer(paginated_queryset, many=True)
    #     return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя

        return Habit.objects.filter(Q(user=self.request.user)|Q(is_public=True))

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsEmptyOwner | IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsEmptyOwner | IsOwner]

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsEmptyOwner | IsOwner]

    def perform_update(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]