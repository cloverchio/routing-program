from model.graph import Graph
from model.location import Location
from service.routing_service import RoutingService


class LocationService:

    def __init__(self, location_data, distance_data):
        self._graph = Graph()
        self._locations = self._to_locations(location_data, distance_data)
        self._graph_locations(self._graph, self._locations)
        self._graph_distances(self._graph, self._locations)

    def get_route(self, starting_location, next_location):
        return RoutingService(self._graph, starting_location).shortest_route(next_location)

    @staticmethod
    def _graph_distances(graph, locations):
        location_len = len(locations)
        for i in range(0, location_len - 1):
            starting_location = locations[i]
            print(starting_location.address)
            for j in range(i + 1, location_len):
                next_location = locations[j]
                graph.add_edge(starting_location.address, next_location.address, next_location.distances[i])

    @staticmethod
    def _graph_locations(graph, locations):
        for location in locations:
            graph.add_vertex(location.address)

    @staticmethod
    def _to_locations(location_data, distance_data):
        locations = []
        for row_index in range(0, len(location_data)):
            location_row = location_data[row_index]
            distances = [float(distance) for distance in distance_data[row_index] if distance != '']
            locations.append(LocationService._to_location(location_row[0], location_row[1], distances))
        return locations

    @staticmethod
    def _to_location(name, address, distances):
        location_distance = Location()
        location_distance.name = name
        location_distance.address = address
        location_distance.distances = distances
        return location_distance
