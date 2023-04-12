# Python Challenge

Challenge for Python Backend developers. For description see INSTRUCTIONS.md.

# Files

## files

* `src/models/trip.py`: Mongodb document definition for storing the penguin trips
* `src/routes/trip_routes/calculate.py`: Calculate route
* `src/routes/trip_routes/business_trip.py`: Business trips route
* `src/routes/trip_routes/utils.py`: helpers functions/Class for 
* `src/routes/trip_routes/schema.py`: Request Schema definition
* `test/test_route_calculate`: test of `/calculate` route
* `test/test_route_business_trips`: test of `/business-trips` route

## Updated files

* `src/routes/add_routes.py`: added `/calculate` and `/business-trips` routes
* `requirements.txt`: added the following packages: requests and marshmallow

# Used algorithm

Based on the given instructions, the main challenge is to find the shortest path to the destinations according to the provided distances with a starting point `Munich` for that we can adopte the dijkstra algorithm which will help us to find the shortest path to destination places where different cites represent nodes, edges are the connections between those cites and the weight is represented by the time in hours between two cities.


