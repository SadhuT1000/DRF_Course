from rest_framework.serializers import ValidationError

import habits
from habits.models import Habit


class WithoutRewardValidator:
    """Исключаем одновременный выбор связанной привычки и указания вознаграждения."""

    def __init__(self, field1, field2):

        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):

        if habits.get("related_habit") and habits.get("reword"):
            raise ValidationError(
                f"В модели не должно быть заполнено одновременно и поле вознаграждения,"
                f" и поле связанной привычки. Можно заполнить только одно из двух полей."
            )


class TimeActionValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field1):

        self.field1 = field1

    def __call__(self, value):

        if habits.get("time_for_action"):
            habit_time = habits.get("time_for_action")
            if habit_time > 120:
                raise ValidationError(
                    "Время выполнения должно быть не больше 120 секунд."
                )


class NiceHabitInAssociatedValidator:
    """
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, habit):

        if habit.get("related_habit"):
            associted_habit = Habit.objects.get(pk=habit.get("related_habit").pk)
            if not associted_habit.good_habit:
                raise ValidationError(
                    f"В связанные привычки могут попадать только привычки с признаком приятной привычки."
                )


class NiceHabitWithoutValidator:
    """
    У приятной привычки не может быть вознаграждения или связанной привычки.
    """

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        if habits.get("good_habit"):
            if habits.get("reward") or habits.get("related_habit"):
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки."
                )


class PeriodHabitValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    def __init__(self, field1):

        self.field1 = field1

    def __call__(self, value):

        if habits.get("periodicity"):
            period_time = habits.get("periodicity")
            if period_time > 7:
                raise ValidationError(
                    "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
                )
