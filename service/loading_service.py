class LoadingService:

    def __init__(self, packaging_service):
        self._packaging_service = packaging_service
        self._truck_two_specific_packages = {3, 18, 36, 38}
        self._dependent_packages = {13, 14, 15, 16, 19, 20}
        self._delayed_packages = {6, 17, 25, 28, 32}
        self._remaining_packages = self._packaging_service.get_all_package_ids() \
            .difference(self._truck_two_specific_packages,
                        self._dependent_packages,
                        self._delayed_packages)

    def load_truck_one(self, truck_one):
        """
        Loads the first truck to capacity with packages.
        :param truck_one: to fill with packages.
        :return:
        """
        truck_one.add_packages(self._packaging_service.get_packages(self._dependent_packages))
        while self._remaining_packages and len(truck_one) < truck_one.capacity:
            truck_one.add_package(self._packaging_service.get_package(self._remaining_packages.pop()))

    def load_truck_two(self, truck_two):
        """
        Loads the second truck to capacity with packages.
        :param truck_two: to fill with packages.
        :return:
        """
        truck_two.add_packages(self._packaging_service.get_packages(self._truck_two_specific_packages))
        while self._remaining_packages and len(truck_two) < truck_two.capacity:
            truck_two.add_package(self._packaging_service.get_package(self._remaining_packages.pop()))

    def load_truck_three(self, truck_three):
        """
        The third truck represents the first or second truck but with the third driver.
        Used when the either of the two active trucks go back to the hub to load
        the delayed packages.
        :param truck_three: to fill with packages.
        :return:
        """
        truck_three.add_packages(self._packaging_service.get_packages(self._delayed_packages))
        while self._remaining_packages and len(truck_three) < truck_three.capacity:
            truck_three.add_package(self._packaging_service.get_package(self._remaining_packages.pop()))
