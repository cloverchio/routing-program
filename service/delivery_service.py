from model.hashtable import HashTable
from service.routing_service import RoutingService


class DeliveryService:

    def __init__(self, starting_location, location_data, distance_data):
        self._starting_location = starting_location
        self._routing_service = RoutingService(location_data, distance_data)
        self._total_distance = 0

    def total_distance(self):
        """
        Retrieves the total distance of the deliveries
        that were performed by the instance of the service.
        :return: total distance covered by the trucks during their deliveries.
        """
        return self._total_distance

    def deliver_packages(self, truck):
        """
        Manages the deliveries for a given truck. Continually updates location
        and package data before eventually making its way back to the hub.
        Total distance is then updated with the truck's mileage.
        :param truck: in which to deliver packages with.
        :return:
        """
        truck.location = self._starting_location
        undelivered_packages = self._undelivered_packages(truck.packaging_service, truck.assigned_packages())
        delivery_route = self._routing_service.get_delivery_route(self._starting_location, undelivered_packages)
        for delivery in delivery_route:
            truck.deliver_package(delivery[0], delivery[2])
        hub_distance = self._routing_service.get_shortest_distance(truck.location, self._starting_location)
        truck.return_to_starting_location(self._starting_location, hub_distance)
        self._total_distance += truck.mileage

    @staticmethod
    def _undelivered_packages(packaging_service, assigned_package_ids):
        undelivered_packages = HashTable(capacity=len(assigned_package_ids) + 1)
        for package_id in assigned_package_ids:
            package = packaging_service.get_package(package_id)
            undelivered_packages.add(package_id, package)
        return undelivered_packages
