from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsListAPIView(ListAPIView):
    """Просмотр списка привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class HabitsCreateAPIView(CreateAPIView):
    """Создание привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsUpdateApiView(UpdateAPIView):
    """Изменнение привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsRetrieveAPIView(RetrieveAPIView):
    """Просмотр конкретной привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]


class HabitPublishedListAPIView(ListAPIView):
    """Вывод опубликованных привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(public_habits=True)
        return queryset
