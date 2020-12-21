from model.delivery import Delivery
from model.graph import Graph
from model.hashtable import HashTable
from model.location import Location
from util.route_util import RouteUtil


class RoutingService:

    def __init__(self, location_data, distance_data):
        self._locations = self._to_locations(location_data, distance_data)
        self._distance_cache = HashTable()
        self._graph = Graph()
        self._graph_locations(self._graph, self._locations)
        self._graph_distances(self._graph, self._locations)

    def get_delivery_route(self, current_location, undelivered_packages):
        """
        Builds a delivery route for the given packages using locally optimal
        addresses to that of the address that was previously delivered to.

        Relates to section A of the requirements.

        :param current_location: current location of the truck.
        :param undelivered_packages: the packages that will need to be delivered.
        :return:
        """
        delivery_route = []
        while undelivered_packages:
            closest_delivery = self.find_closest_delivery(current_location, undelivered_packages)
            delivery_route.append(closest_delivery)
            current_location = closest_delivery.address
            undelivered_packages.remove(closest_delivery.package_id)
        return delivery_route

    def find_closest_delivery(self, current_location, undelivered_packages):
        """
        Finds the package address with the smallest distance to that of the current location.
        :param current_location: the current location in which to deliver from.
        :param undelivered_packages: in which to find the next closest delivery.
        :return:
        """
        deliveries = []
        for package in undelivered_packages.values():
            shortest_distance = self.get_shortest_distance(current_location, package.address)
            deliveries.append(Delivery(package.id, package.address, shortest_distance))
        return min(deliveries, key=lambda delivery: delivery.distance)

    def get_shortest_distance(self, origin, destination):
        """
        Finds the shortest distance between two given locations.
        :param origin: the origin location.
        :param destination: the destination location.
        :return: the shortest distance between the origin and the destination.
        """
        cache_key = (origin, destination)
        if cache_key in self._distance_cache:
            return self._distance_cache.get(cache_key)
        shortest_route = RouteUtil(self._graph, origin).shortest_route(destination)
        shortest_distance = sum([vertex.distance for vertex in shortest_route])
        self._distance_cache.add(cache_key, shortest_distance)
        return shortest_distance

    @staticmethod
    def _graph_distances(graph, locations):
        location_len = len(locations)
        for i in range(0, location_len - 1):
            starting_location = locations[i]
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
            locations.append(RoutingService._to_location(location_row[0], location_row[1], distances))
        return locations

    @staticmethod
    def _to_location(name, address, distances):
        location_distance = Location()
        location_distance.name = name
        location_distance.address = address
        location_distance.distances = distances
        return location_distance
