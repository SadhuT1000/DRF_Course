from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )

    place = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Место для выполнения привычки",
        help_text="Напиши место",
    )

    time_for_habit = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Время",
        help_text="Время для выполнения привычки",
    )

    action = models.CharField(
        max_length=150,
        verbose_name="Действие",
        help_text="Напиши что делаешь",
    )

    good_habit = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name="Признак полезной привычки",
        help_text="привычка, которую можно привязать "
        "к выполнению полезной привычки.",
    )

    related_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    reword = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="чем пользователь должен себя вознаградить после выполнения",
    )

    periodicity = models.IntegerField(
        default=1,
        verbose_name="Периодичность",
        null=True,
        blank=True,
        help_text="Укажите кол-во дней, за которые необходимо выполнить привычку (по умолчанию раз в день)",
    )

    time_for_action = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Время на действие",
        help_text="время, которое предположительно потратит пользователь на выполнение привычки",
    )

    public_habits = models.BooleanField(
        default=True, null=True, blank=True, verbose_name="Признак публичности"
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action}"
