# flake8: noqa
from django.conf.urls.static import static
from django.urls import path

from config import settings
from habits.apps import HabitsConfig
from habits.views import (HabitPublishedListAPIView, HabitsCreateAPIView,
                          HabitsDestroyAPIView, HabitsListAPIView,
                          HabitsRetrieveAPIView, HabitsUpdateApiView)

app_name = HabitsConfig.name


urlpatterns = [
    path("habits/", HabitsListAPIView.as_view(), name="habits_list"),
    path("habits/<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("habits/create/", HabitsCreateAPIView.as_view(), name="habits_create"),
    path(
        "habits/<int:pk>/update/", HabitsUpdateApiView.as_view(), name="habits_update"
    ),
    path(
        "habits/<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habits_delete"
    ),
    path("published/", HabitPublishedListAPIView.as_view(), name="published"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
