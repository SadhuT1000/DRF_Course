from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner
from habits.models import Habit
from habits.serializers import HabitsSerializer


class HabitsListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated)

class HabitsCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsAuthenticated)


class HabitsUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]




class HabitPublishedListAPIView(ListAPIView):
    """Вывод опубликованных привычек """
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    #pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset




