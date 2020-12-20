from model.hashtable import HashTable
from service.loading_service import LoadingService
from service.packaging_service import PackagingService
from service.routing_service import RoutingService


class DeliveryService:

    def __init__(self, starting_location, location_data, distance_data, package_data):
        self._packaging_service = PackagingService(package_data)
        self._loading_service = LoadingService(self._packaging_service)
        self._routing_service = RoutingService(location_data, distance_data)
        self._starting_location = starting_location
        self._total_mileage = 0

    def package_status_by_time(self, time):
        """
        Retrieves the string representation of all packages at the
        given time. Uses the delivery status that would have correlated with
        that time. Should satisfy the requires of section G.
        :param time: in which to retrieve the status of the packages.
        :return:
        """
        packages = self._packaging_service.get_all_packages()
        return [package.status_by_time(time) for package in packages]

    def package_status(self, package_id):
        """
        Retrieves the string representation of the package, which should have 
        all of the elements required to satisfy section F.
        :param package_id: in which to retrieve package data for.
        :return:
        """
        return str(self._packaging_service.get_package(package_id))

    def total_mileage(self):
        """
        Retrieves the total mileage of the deliveries
        that were performed by the instance of the service.
        :return: total distance covered by the trucks during their deliveries.
        """
        return self._total_mileage

    def load_packages(self, trucks):
        """
        Manages the loading of packages onto the trucks.
        Delegates to the loading service for assigning the appropriate
        ids to each truck.
        :param trucks: in which to load packages onto.
        :return:
        """
        for truck in trucks:
            truck.packaging_service = self._packaging_service
            if truck.id == 1:
                self._loading_service.load_truck_one(truck)
            if truck.id == 2:
                self._loading_service.load_truck_two(truck)
            if truck.id == 3:
                self._loading_service.load_truck_three(truck)

    def deliver_packages(self, truck, start_time):
        """
        Manages the deliveries for a given truck. Continually updates location
        and package data before eventually making its way back to the hub.
        Total distance is then updated with the truck's mileage.
        :param truck: in which to deliver packages with.
        :param start_time: the delivery start time.
        :return:
        """
        truck.current_time = start_time
        truck.location = self._starting_location
        undelivered_packages = self._undelivered_packages(truck.packaging_service, truck.assigned_packages())
        delivery_route = self._routing_service.get_delivery_route(self._starting_location, undelivered_packages)
        for delivery in delivery_route:
            truck.deliver_package(delivery[0], delivery[2])
        hub_distance = self._routing_service.get_shortest_distance(truck.location, self._starting_location)
        truck.return_to_starting_location(self._starting_location, hub_distance)
        self._total_mileage += truck.mileage

    @staticmethod
    def _undelivered_packages(packaging_service, assigned_package_ids):
        undelivered_packages = HashTable(capacity=len(assigned_package_ids) + 1)
        for package_id in assigned_package_ids:
            package = packaging_service.get_package(package_id)
            undelivered_packages.add(package_id, package)
        return undelivered_packages
