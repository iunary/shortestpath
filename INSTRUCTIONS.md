# Python challenge

# Introduction

Our penguins love to travel! There are two specific situations when they travel most:
* to see new places on vacations (`casual` trips)
* to visit clients (`business` trips)

In order to help them, we are developing a platform to minimize travel time, so they can spend more time at their final destination.

# Challenge

Your job here, as a backend developer, is to extend our basic API by adding two routes:

* `/calculate`: find all places that must be visited in order to minimize the travel time for the given input.
* `/business-trips`: returns business information from already calculated trips, so we can think of new strategies to help our employees.

The routes must follow the [Routes documentation](#routes-documentation).

# Deliverables

1. A **README** file explaining any modifications, decisions, and algorithms used.

2. A zip file containing the whole project. If possible, remove the **virtual env**.

# Routes documentation

### `/calculate`
* Only allows `POST`, expects a `JSON` as input and returns a `JSON`.
* The starting point is always `Munich`.
* There is no cost to travel to the current city (Ex. Munich to Munich the travel time is 0).
* The travel time is given in hours, and is always an `integer`.
* The time from `place A` to `place B`, and `place B` to `place A` is the same.
* Just consider one-way trip: ignore the return time to Munich.
* The destinations order is important! Is totally fine (and sometimes expected) to visit some places before they being the target destination, it doesn't exclude them from the destination list. (e.g.: for given destinations: `Munich` -> `Kinganru` -> `SantaTiesrie` the places to travel can be: `Munich` -> **SantaTiesrie** -> `Kinganru` -> `SantaTiesrie`)

#### Payload:

JSON with fields:
* **name**(`str`): penguin name.
* **destinations**(`List[str]`): list of destinations.
* **business**(`bool`): indicates if it is a business trip. `true` for a business trip, `false` for a "casual" trip.
* **distances**(`List[str]`): list with distances between places.

##### Example

```json
{
    "name": "Alanto",
    "destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
    "business": true,
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
        "SantaTiesrie - Mitling: 2"
    ]
}
```

For this example the distances are:
* Munich to Munich: 0 hour
* Munich to Kinganru: 3 hours
* Munich to Facenianorth: 7 hours
* Munich to SantaTiesrie: 4 hours
* Munich to Mitling: 1 hour
* Kinganru to Facenianorth: 2 hours
* Kinganru to SantaTiesrie: 1 hour
* Kinganru to Mitling: 1 hour
* Facenianorth to SantaTiesrie: 5 hours
* Facenianorth to Mitling:  3 hours
* SantaTiesrie to Mitling: 2 hours


#### Returns:
Json with fields:
* **places_to_travel**(`List[str]`): list with all places to visit.

##### Example

```json
{
   "places_to_travel": ["Munich", "Mitling", "Kinganru", "Facenianorth", "Kinganru", "SantaTiesrie"]
}
```

### `/business-trips`
* Only allows GET and expects a JSON as result.
* Should contain information ONLY about business trips, ignoring casual trips.

#### Returns:

Json with fields:
* **penguins_with_most_trips**(`List[str]`): penguins with most business trips. If more than one penguin has the same number of trips, all of them must be on the list.
* **most_visited_places**(`List[str]`): places that appear most as destinations (only places in `destinations` from the `/calculate` payload!). If more than one place has a bigger number of visits, all of them must be returned.
* **total_business_trips**(`int`): total number of business trips.

##### Example

If the given example for `/calculate` run 3 times, the business route should returns:

`Returns`:
```json
{
    "penguins_with_most_trips": ["Alanto"],
    "most_visited_places": ["Kinganru", "Facenianorth", "SantaTiesrie"],
    "total_business_trips": 3
}
```

# How to run

A base API with a DB connection already exists at `docker-compose.yml`.

To run, execute the following command:

   > `docker-compose rm -f; docker-compose -f docker-compose.yml up --build --force-recreate`

(It will clean up existing containers and force them to be recreated)
 
To test your API you can check `http://127.0.0.1:8001/` on your browser.

To run the example, run the script: `example.py` (`requests` lib is necessary)


## How to test

Install dependencies:
1. Create a virtual env and activate it: `python3 -m venv env; source env/bin/activate`
2. Install dependencies: `pip install -r requirements.txt -r dev-requirements.txt`
3. Run tests: `pytest test/`

# Notes
* Feel free to use any 3rd-party library, just remember to justify the decision.
* The code must be compatible with python3.8
* The API must run using Flask (already set on the base source code)
* The database must be MongoDB (already set on the base source code)
* To test, the docker-compose setup will be invoked, so guarantee it works (or add a note about it in the README).

Happy coding!
