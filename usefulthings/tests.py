from datetime import datetime, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from usefulthings.models import Wont
from users.models import User


class WontTestCase(APITestCase):
    def setUp(self):
        """Функция подготовки данных перед тестированием"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)  # авторизуем пользователя
        self.wont = Wont.objects.create(
            owner=self.user,
            place="тест",
            time="07:00:00",
            action="тест",
            is_pleasant=False,
            period=1,
            award="тестовое вознаграждение",
            time_to_action=timedelta(seconds=60),
        )

    def test_wont_create(self):
        """Тестирование создания экземпляра привычки"""
        url = reverse("usefulthings:wont-create")
        data = {
            "place": "test",
            "time": "05:00:00",
            "action": "test",
            "period": 1,
            "time_to_action": timedelta(seconds=60),
        }
        response = self.client.post(url, data)
        print(datetime.now())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wont.objects.all().count(), 2)

    def test_wont_list(self):
        """Тестирование запроса на вывод списка привычек"""
        url = reverse("usefulthings:wont-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Wont.objects.all().count(), 1)

    def test_wont_retrieve(self):
        """Тестирование запроса на вывод полей привычки по заданному pk"""
        url = reverse("usefulthings:wont-retrieve", args=(self.wont.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.wont.action)

    def test_wont_update(self):
        """Тестирование запроса на изменение полей привычки"""
        url = reverse("usefulthings:wont-update", args=(self.wont.pk,))
        data_update = {
            "place": "тест",
            "action": "тест",
            "is_pleasant": False,
            "period": 1,
            "award": "тестовое вознаграждение",
            "time": "05:05:00",
            "time_to_action": timedelta(seconds=65),
        }
        response = self.client.patch(url, data=data_update)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("time"), "05:05:00")

    def test_wont_delete(self):
        """Тестирование запроса на удаление привычки с заданным pk"""
        url = reverse("usefulthings:wont-delete", kwargs={"pk": self.wont.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Wont.objects.all().count(), 0)
