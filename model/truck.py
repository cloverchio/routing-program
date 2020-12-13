from model.package import DeliveryStatus, Priority


class TruckAtCapacityError(ValueError):
    pass


class TruckEmptyError(ValueError):
    pass


class Truck:

    def __init__(self, truck_id=None, driver=None, location=None, speed=18, capacity=16):
        self._id = truck_id
        self._driver = driver
        self._starting_location = location
        self._location = location
        self._speed = speed
        self._capacity = capacity
        self._undelivered_priority_packages = []
        self._undelivered_packages = []
        self._delivered_packages = []
        self._mileage = 0
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, item):
        if item in self._undelivered_packages:
            return True
        return False

    def next_priority_location(self):
        next_priority_package = self._undelivered_priority_packages[-1]
        if next_priority_package is not None:
            return next_priority_package.address
        return None

    def next_location(self):
        next_package = self._undelivered_packages[-1]
        if next_package is not None:
            return next_package.address
        return None

    def undelivered_priority_packages(self):
        return self._undelivered_priority_packages

    def undelivered_packages(self):
        return self._undelivered_packages

    def delivered_packages(self):
        return self._delivered_packages

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, truck_id):
        self._id = truck_id

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage

    def has_capacity(self):
        """
        Used to determine whether or not there is still space
        on the truck.
        :return:
        """
        return self._size < self._capacity

    def add_packages(self, packages):
        """
        Adds multiple packages to the undelivered queue.
        :param packages: to be added to the undelivered queue.
        :return:
        """
        for package in packages:
            self.add_package(package)

    def add_package(self, package):
        """
        Adds a single package to the undelivered queue if the truck is not at capacity.
        :param package: to be added to the undelivered queue.
        :return:
        """
        if self._size + 1 > self._capacity:
            raise TruckAtCapacityError("truck is at capacity")
        package.status = DeliveryStatus.EN_ROUTE
        if package.priority == Priority.HIGH:
            self._undelivered_priority_packages.append(package)
        else:
            self._undelivered_packages.append(package)
        self._size += 1

    def deliver_priority_package(self, distance):
        """
        Removes a package from the undelivered priority queue if the truck is not empty.
        Updates delivery status, truck location, and distance.
        :param distance: distance of the route taken to deliver the package.
        :return:
        """
        self._deliver_package(distance, self._undelivered_priority_packages)

    def deliver_package(self, distance):
        """
        Removes a package from the undelivered queue if the truck is not empty.
        Updates delivery status, truck location, and distance.
        :param distance: distance of the route taken to deliver the package.
        :return:
        """
        self._deliver_package(distance, self._undelivered_packages)

    def return_to_starting_location(self, distance):
        """
        Represents the truck traveling to its original location (the hub for example).
        Sets the truck location to the starting location and updates the distance.
        :param distance: to the starting location from the truck's current location.
        :return:
        """
        self._mileage += distance
        self._location = self._starting_location

    def sort_priority_packages(self):
        """
        Sorts undelivered priority packages by their deadlines.
        This is so the higher priority packages are more easily accessible
        at the back of the truck.
        :return:
        """
        self._undelivered_priority_packages = sorted(self._undelivered_priority_packages,
                                                     key=lambda package: package.deadline,
                                                     reverse=True)

    def _deliver_package(self, distance, undelivered_packages):
        if self._size == 0:
            raise TruckEmptyError("truck is empty")
        delivered = undelivered_packages.pop()
        delivered.status = DeliveryStatus.DELIVERED
        self._size -= 1
        self._mileage += distance
        self._location = delivered.address
        self._delivered_packages.append(delivered)
