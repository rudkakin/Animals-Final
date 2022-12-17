from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class HtmlApiTest(APITestCase):

    def test_response_correct1(self):
        url = reverse(viewname='api')
        response = self.client.get(url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
            {'Unnamed: 0': {0: 2, 1: 0, 2: 4, 3: 1, 4: 3}, 'id': {0: 3, 1: 1, 2: 5, 3: 2, 4: 4}, 'Name': {0: 'Слон', 1: 'Лев', 2: 'Волк', 3: 'Черепаха', 4: 'Утконос'}, 'Type': {0: 'Млекопитающий', 1: 'Хищник', 2: 'Хищник', 3: 'Пресмыкающий', 4: 'Водоплавающее млекопитающее'}, 'Colour': {0: 'Серый', 1: 'Рыжий', 2: 'Белый', 3: 'Зеленый', 4: 'Коричневый'}, 'Size': {0: 350, 1: 150, 2: 90, 3: 70, 4: 50}}
        )
    def test_response_correct2(self):
        url = reverse(viewname='api')
        response = self.client.get(url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data,
            {'named: 0': {0: 2, 1: 0, 2: 4, 3: 1, 4: 3}, 'id': {0: 3, 1: 1, 2: 5, 3: 2, 4: 4}, 'Name': {0: 'Слон', 1: 'Лев', 2: 'Волк', 3: 'Черепаха', 4: 'Утконос'}, 'Type': {0: 'Млекопитающий', 1: 'Хищник', 2: 'Хищник', 3: 'Пресмыкающий', 4: 'Водоплавающее млекопитающее'}, 'Colour': {0: 'Серый', 1: 'Рыжий', 2: 'Белый', 3: 'Зеленый', 4: 'Коричневый'}, 'Size': {0: 350, 1: 150, 2: 90, 3: 70, 4: 50}}
        )
    def test_response_correct3(self):
        url = reverse(viewname='api')
        response = self.client.get(url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data,
            {'Unnamed: 0': {0: 2, 1: 0, 2: 4, 3: 1, 4: 3}, 'id': {0: 3, 1: 1, 2: 5, 3: 2, 4: 4}, 'Name': {0: 'Пантера', 1: 'Лев', 2: 'Волк', 3: 'Черепаха', 4: 'Утконос'}, 'Type': {0: 'Млекопитающий', 1: 'Хищник', 2: 'Хищник', 3: 'Пресмыкающий', 4: 'Водоплавающее млекопитающее'}, 'Colour': {0: 'Серый', 1: 'Рыжий', 2: 'Белый', 3: 'Зеленый', 4: 'Коричневый'}, 'Size': {0: 350, 1: 150, 2: 90, 3: 70, 4: 50}}
        )
    def test_response_correct4(self):
        url = reverse(viewname='api')
        response = self.client.get(url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data,
            {'Unnamed: 0': {0: 2, 1: 0, 2: 4, 3: 1, 4: 3}, 'id': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, 'Name': {0: 'Слон', 1: 'Лев', 2: 'Волк', 3: 'Черепаха', 4: 'Утконос'}, 'Type': {0: 'Млекопитающий', 1: 'Хищник', 2: 'Хищник', 3: 'Пресмыкающий', 4: 'Водоплавающее млекопитающее'}, 'Colour': {0: 'Серый', 1: 'Рыжий', 2: 'Белый', 3: 'Зеленый', 4: 'Коричневый'}, 'Size': {0: 350, 1: 150, 2: 90, 3: 70, 4: 50}}
        )
    def test_response_correct5(self):
        url = reverse(viewname='api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class ViewsTestCase(TestCase):
    def test_1(self):
        response = self.client.get('Rudkin')
        self.assertEqual(response.status_code, 404)

    def test_2(self):
        url1 = reverse('home')
        response = self.client.get(url1)
        self.assertEqual(response.status_code, 200)

    def test_3(self):
        response = self.client.get('Ilya')
        self.assertNotEqual(response.status_code, 200)

    def test_4(self):
        response = self.client.get('XXX')
        self.assertNotEqual(response.status_code, 401)

    def test_5(self):
        response = self.client.get('INBO')
        self.assertNotEqual(response.status_code, 400)