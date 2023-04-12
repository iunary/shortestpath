import json
from unittest import TestCase

from mongoengine import connect, disconnect
from flask import Flask

from src.routes import add_routes


class TestRouteBurinessTrips(TestCase):
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

    def test_business_trips(self):
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

        business_trips_want = {
            "penguins_with_most_trips": ["Alanto"],
            "most_visited_places": ["Kinganru", "Facenianorth", "SantaTiesrie"],
            "total_business_trips": 1,
        }

        with self.app.test_client() as test_client:
            response = test_client.post(
                "/calculate",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
            )
            self.assertEqual(response.status_code, 201)
            self.assertDictEqual(json.loads(response.data), want)

            response = test_client.get("/business-trips")
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(json.loads(response.data), business_trips_want)
