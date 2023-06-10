import json

from django.test import TestCase, Client

from .models import Board

class BoardTest(TestCase):
    def setUp(self):
        Board.objects.bulk_create(
            [
                Board(
                    title=f"Test title{i+1}",
                    content="Test content"
                ) for i in range(5)
            ]
        )

    def tearDown(self) -> None:
        Board.objects.all().delete()
        return super().tearDown()
    
    def test_create_board(self):
        client = Client()
        data = {
            "title": "Test Create title",
            "content": "Test Create Content"
        }
        response = client.post(
            "/boards", json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

    def test_get_board_list(self):
        client = Client()
        response = client.get(
            "/boards"
        )

        self.assertEqual(response.status_code, 200)

    def test_get_board(self):
        client = Client()
        response = client.get(
            "/boards/1"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id": 1,
            "title": "Test title1",
            "content": "Test content"
        })
