class DeliveryService:

    def __init__(self, starting_location, location_service):
        self._starting_location = starting_location
        self._location_service = location_service
        self._total_distance = 0

    def total_distance(self):
        """
        Retrieves the total distance of the deliveries
        that were performed by the instance of the service.
        :return: total distance covered by the trucks during the deliveries.
        """
        return self._total_distance

    # TODO improve performance of this section
    def deliver_packages(self, truck):
        """
        Delivers the packages assigned to the given truck
        and returns to the hub when all of the deliveries
        have been made.
        :param truck: to deliver packages with.
        :return:
        """
        truck.location = self._starting_location
        self._deliver_packages(truck, truck.undelivered_priority_packages(), truck.deliver_priority_package)
        self._deliver_packages(truck, truck.undelivered_packages(), truck.deliver_package)
        start_distance = self._location_service.get_shortest_distance(truck.location, self._starting_location)
        truck.return_to_starting_location(start_distance)
        self._total_distance += truck.mileage

    def _deliver_packages(self, truck, undelivered_packages, deliver):
        while undelivered_packages:
            priority_packages = undelivered_packages.values()
            closest_delivery = self._find_closest_delivery(truck.location, priority_packages)
            deliver(closest_delivery[0], closest_delivery[1])

    def _find_closest_delivery(self, current_location, undelivered_packages):
        distances = []
        for package in undelivered_packages:
            shortest_distance = self._location_service.get_shortest_distance(current_location, package.address)
            distances.append((package.id, shortest_distance, package.address))
        return min(distances, key=lambda distance: distance[1])
