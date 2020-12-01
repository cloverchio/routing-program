class TruckAtCapacityError(ValueError):
    pass


class Truck:

    def __init__(self, driver, location, speed=18, capacity=16):
        self._driver = driver
        self._location = location
        self._speed = speed
        self._capacity = capacity
        self._total_distance = 0
        self._size = 0
        self.undelivered = []
        self.delivered = []

    def __len__(self):
        return self._size

    def __contains__(self, item):
        if item in self.undelivered:
            return True
        return False

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
    def total_distance(self):
        return self._total_distance

    @total_distance.setter
    def total_distance(self, total_distance):
        self._total_distance = total_distance

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
        self.undelivered.append(package)
        self._size += 1
