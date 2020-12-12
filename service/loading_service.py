class LoadingService:

    def __init__(self, packaging_service):
        self._packaging_service = packaging_service
        # manually categorizing packages as suggested by the course instructions...
        # packages that need to be delivered by truck 2
        self._truck_two_specific_packages = {3, 18, 36, 38}
        # packages that have dependencies on each other
        self._dependent_packages = {13, 14, 15, 16, 19, 20}
        # packages that have been delayed
        self._delayed_packages = {6, 17, 25, 28, 32}
        # packages that have wrong address
        self._wrong_address_packages = {9}
        # packages that have a strict deadline and haven't been previously categorized
        self._prioritized_packages = {1, 6, 13, 14, 15, 16, 20, 25, 29, 30, 31, 34, 37, 40} \
            .difference(self._truck_two_specific_packages,
                        self._dependent_packages,
                        self._delayed_packages,
                        self._wrong_address_packages)
        # remaining packages
        self._remaining_packages = self._packaging_service.get_all_package_ids() \
            .difference(self._truck_two_specific_packages,
                        self._dependent_packages,
                        self._delayed_packages,
                        self._wrong_address_packages,
                        self._prioritized_packages)

    def load_trucks(self, truck_one, truck_two, truck_three):
        self._load_truck_one(truck_one)
        self._load_truck_two(truck_two)
        self._load_truck_three(truck_three)

    def _load_truck_one(self, truck_one):
        """
        Loads the first truck to capacity with packages.
        :param truck_one: to fill with packages.
        :return:
        """
        truck_one.add_packages(self._packaging_service.get_packages(self._dependent_packages))
        truck_one.add_packages(self._packaging_service.get_packages(self._prioritized_packages))
        while self._remaining_packages and truck_one.has_capacity():
            truck_one.add_package(self._packaging_service.get_package(self._remaining_packages.pop()))
        truck_one.sort_undelivered_packages()

    def _load_truck_two(self, truck_two):
        """
        Loads the second truck to capacity with packages.
        :param truck_two: to fill with packages.
        :return:
        """
        truck_two.add_packages(self._packaging_service.get_packages(self._truck_two_specific_packages))
        truck_two.add_packages(self._packaging_service.get_packages(self._delayed_packages))
        while self._remaining_packages and truck_two.has_capacity():
            truck_two.add_package(self._packaging_service.get_package(self._remaining_packages.pop()))
        truck_two.sort_undelivered_packages()

    def _load_truck_three(self, truck_three):
        """
        The third truck represents the first or second truck but with the third driver.
        Used when either of the two active trucks go back to the hub to load
        the remaining packages.
        :param truck_three: to fill with packages.
        :return:
        """
        truck_three.add_packages(self._packaging_service.get_packages(self._wrong_address_packages))
        while self._remaining_packages and truck_three.has_capacity():
            truck_three.add_package(self._packaging_service.get_package(self._remaining_packages.pop()))
