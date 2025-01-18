from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (NiceHabitInAssociatedValidator,
                               NiceHabitWithoutValidator, PeriodHabitValidator,
                               TimeActionValidator, WithoutRewardValidator)


class HabitsSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        valodators = [
            WithoutRewardValidator(field1="related_habit", field2="reward"),
            TimeActionValidator(field1="time_for_action"),
            NiceHabitInAssociatedValidator(field1="related_habit"),
            NiceHabitWithoutValidator(
                field1="good_habit", field2="reward", field3="related_habit"
            ),
            PeriodHabitValidator(field1="periodicity"),
        ]
