# flake8: noqa


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    """Тестировка CRUD привычек"""

    def setUp(self):

        self.user = User.objects.create(
            email="admin@example.com", is_staff=True, is_superuser=True, is_active=True
        )
        self.habits = Habit.objects.create(action="test_habit", user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Детальный просмотр"""
        url = reverse("habits:habits_retrieve", args=(self.habits.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habits.action)

    def test_habit_create(self):
        """Создание привычки"""
        url = reverse("habits:habits_create")
        data = {"action": "test_habit2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Детальный просмотр"""
        url = reverse("habits:habits_update", args=(self.habits.pk,))
        data = {"action": "test_habit2"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "test_habit2")

    def test_habit_delete(self):
        """Удаление привычки"""

        url = reverse("habits:habits_delete", args=(self.habits.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Список привычек"""
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habits.pk,
                    "place": None,
                    "time_for_habit": None,
                    "action": "test_habit",
                    "good_habit": False,
                    "reword": None,
                    "periodicity": 1,
                    "time_for_action": None,
                    "public_habits": True,
                    "user": self.user.pk,
                    "related_habit": None,
                },
            ],
        }

        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_list_published(self):
        """Список опубликованных привычек"""
        url = reverse("habits:published")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habits.pk,
                    "place": None,
                    "time_for_habit": None,
                    "action": "test_habit",
                    "good_habit": False,
                    "reword": None,
                    "periodicity": 1,
                    "time_for_action": None,
                    "public_habits": True,
                    "user": self.user.pk,
                    "related_habit": None,
                },
            ],
        }

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
