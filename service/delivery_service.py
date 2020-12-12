class DeliveryService:

    def __init__(self, starting_location, location_service):
        self._starting_location = starting_location
        self._location_service = location_service
        self._total_distance = 0

    def total_distance(self):
        """
        Retrieves the total distance of the deliveries
        that were performed by the instance of the service.
        :return: total distance covered by the deliveries.
        """
        return self._total_distance

    def deliver_packages(self, truck):
        """
        Delivers the packages assigned to the given truck
        and returns to the hub when all of the deliveries
        have been made.
        :param truck: to deliver packages with.
        :return:
        """
        truck.location = self._starting_location
        while len(truck) > 0:
            shortest_distance = self._location_service.get_shortest_distance(truck.location, truck.next_location)
            truck.deliver_package(shortest_distance)
        truck.return_to_starting_location(
            self._location_service.get_shortest_distance(truck.location, self._starting_location))
        self._total_distance += truck.total_distance
