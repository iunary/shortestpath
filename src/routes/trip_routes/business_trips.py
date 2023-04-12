from typing import Tuple, Dict, List
from src.models import Trip
from .utils import (
    get_most_visited_places,
    get_penguins_with_most_trips,
    get_total_business_trips,
)


def business_trips() -> Tuple[Dict, int]:
    """Get information about business trips only

    Returns: tuple of dict with response and status code
    """
    trips: List = Trip.objects().filter(business=True)  # get only business trips
    penguins_with_most_trip = get_penguins_with_most_trips(trips)
    most_visited_places = get_most_visited_places(trips)
    total_business_trips = get_total_business_trips(trips)

    return {
        "penguins_with_most_trips": penguins_with_most_trip,
        "most_visited_places": most_visited_places,
        "total_business_trips": total_business_trips,
    }, 200
