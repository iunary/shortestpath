import sys
from typing import List, Dict


class Graph:
    """Graph
    """

    start_node = "Munich"

    def __init__(
        self,
        nodes: List[str],
        destinations: List[str],
        graph: Dict[str, Dict[str, int]],
    ) -> None:
        self.nodes = nodes
        self.graph = graph
        self.destinations = destinations
        self.path = []

    def get_connections(self, node: str) -> List[str]:
        """Return the list of the node connections"""
        connections = []
        for item in self.nodes:
            if self.graph[node].get(item, False):
                connections.append(item)
        return connections

    def get_distance(self, first_node: str, second_node: str) -> int:
        """Return the value of an edge between two nodes"""
        return self.graph[first_node][second_node]

    def __calculate_path(self, start_node: str) -> Dict:
        """dijkstra algorithm implementation"""
        unvisited_nodes = self.nodes.copy()
        shortest_path = {}
        previous_nodes = {}

        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value

        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            connections = self.get_connections(current_min_node)
            for connection in connections:
                val = shortest_path[current_min_node] + self.get_distance(
                    current_min_node, connection
                )
                if val < shortest_path[connection]:
                    shortest_path[connection] = val
                    previous_nodes[connection] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return previous_nodes

    def __get_shortest_path(self, start_node: str, target_node: str) -> List[str]:
        """Return the shortest path between two nodes"""
        previous_nodes = self.__calculate_path(start_node=start_node)
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        self.path += list(reversed(path))
        return self.path

    def get_result(self) -> List:
        """Return the result"""
        self.__get_shortest_path(
            start_node=self.start_node, target_node=self.destinations[0]
        )
        start_node = self.destinations[0]
        for destination in self.destinations:
            self.__get_shortest_path(
                start_node=start_node, target_node=destination)
            start_node = destination
        self.path.insert(0, self.start_node)

        return self.path


def get_nodes(distances: List[str]) -> List[str]:
    """Get all nodes from distances

    Args:
        distances: distances list

    Returns:
        nodes (list[str]): list of the all nodes from distances
    """
    nodes = set()
    for item in distances:
        pairs = item.split(":")[0].split("-")
        for node in pairs:
            nodes.add(node.strip())
    return list(nodes)


def get_graph(distances: List[str]) -> Dict[str, Dict[str, int]]:
    """Build the symmetrical graph from distances
    Args:
        distances (list[str]): list of distances

    Returns:
        graph (dict[str, dict[str, int]]): symmetrical graph from distances
    """
    graph = {}
    for d in distances:
        source, destination, distance_str = (
            d.split("-")[0].strip(),
            d.split("-")[1].split(":")[0].strip(),
            d.split(":")[1].strip(),
        )
        distance = int(distance_str)
        if source not in graph:
            graph[source] = {}
        graph[source][destination] = distance
        if destination not in graph:
            graph[destination] = {}
        graph[destination][source] = distance
    return graph


def get_penguins_with_most_trips(trips: List) -> List[str]:
    """Get penguins with most trips

    Args:
        trips (list): the list of the trips
    Returns:
        penguins_with_most_trips (list[str]): list of penguins with most trips
    """
    names = {}
    for trip in trips:
        name = trip["name"]
        if name not in names:
            names[name] = 1
        else:
            names[name] += 1

    penguins_with_most_trips = [
        k for k, v in names.items() if v == max(names.values())]
    return penguins_with_most_trips


def get_most_visited_places(trips: List) -> List[str]:
    """Get most visited places
    Args:
        trips list: the list of the trips

    Returns:
        most_visited_places (list[str]): list of most visited places
    """
    places = {}
    for trip in trips:
        destinations = trip["destinations"]
        for d in destinations:
            if d not in places:
                places[d] = 1
            else:
                places[d] += 1
    most_visited_places = [
        k for k, v in places.items() if v == max(places.values())]
    return most_visited_places


def get_total_business_trips(trips: List) -> int:
    """Get total business trips
    Args:
        trips list: the list of the trips

    Returns:
        total (int): total number of business trips
    """
    total = len(trips)
    return total
