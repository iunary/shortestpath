from typing import Dict, Tuple
from flask import request
from marshmallow import ValidationError
from src.models import Trip
from .utils import Graph, get_graph, get_nodes
from .schema import TripRequestSchema


def calculate() -> Tuple[Dict, int]:
    """Find all places that must be visited in order to minimize the travel time for the given input

    Returns: tupe of dict with response and status code
    """

    schema = TripRequestSchema()
    try:
        payload = schema.load(request.json)
    except ValidationError as e:
        return e.messages, 400

    name = payload["name"]
    business = payload["business"]
    destinations = payload["destinations"]
    distances = payload["distances"]

    nodes = get_nodes(distances)
    graph = get_graph(distances)

    path = Graph(nodes, destinations, graph)
    result = path.get_result()

    # save the trip
    try:
        trip = Trip(
            name=name,
            business=business,
            destinations=destinations,
            places_to_travel=result,
        )
        trip.save(validate=True)
    except Exception:
        return {"message": "an error occured while trying to save the trip."}, 500

    return {"places_to_travel": result}, 201
