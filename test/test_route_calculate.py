import json
from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask

from src.routes import add_routes


class TestRouteCalculate(TestCase):
    @classmethod
    def setUpClass(cls):
        connect(
            "9fe2c4e93f654fdbb24c02b15259716c",
            uuidRepresentation="standard",
            host="mongomock://localhost",
        )

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def setUp(self):
        self.app = Flask(__name__)
        add_routes(self.app)

    def test_calculate(self):
        """Test calculate"""
        payload = {
            "name": "Alanto",
            "destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
            "business": True,
            "distances": [
                "Munich - Munich: 0",
                "Munich - Kinganru: 3",
                "Munich - Facenianorth: 7",
                "Munich - SantaTiesrie: 4",
                "Munich - Mitling: 1",
                "Kinganru - Facenianorth: 2",
                "Kinganru - SantaTiesrie: 1",
                "Kinganru - Mitling: 1",
                "Facenianorth - SantaTiesrie: 5",
                "Facenianorth - Mitling:  3",
                "SantaTiesrie - Mitling: 2",
            ],
        }

        want = {
            "places_to_travel": [
                "Munich",
                "Mitling",
                "Kinganru",
                "Facenianorth",
                "Kinganru",
                "SantaTiesrie",
            ]
        }

        with self.app.test_client() as test_client:
            response = test_client.post(
                "/calculate",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
            )
            self.assertEqual(response.status_code, 201)
            self.assertEqual(json.loads(response.data), want)
