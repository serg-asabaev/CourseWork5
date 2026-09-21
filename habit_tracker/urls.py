from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from config.settings import MEDIA_ROOT, MEDIA_URL, DEBUG
from habit_tracker.apps import HabitTrackerConfig
from . import views

app_name = HabitTrackerConfig.name

urlpatterns = [
    path('habit/list/', views.HabitListAPIView.as_view(), name='habit_list'),
    path('habit/create/', views.HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', views.HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/update/<int:pk>/', views.HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', views.HabitDestroyAPIView.as_view(), name='habit_delete'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
