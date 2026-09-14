from django.contrib import admin
from django.urls import path

from habit_tracker.apps import HabitTrackerConfig
from . import views

app_name = HabitTrackerConfig.name

urlpatterns = [
    path('', views.HabitListAPIView.as_view(), name='habit_list'),
]
