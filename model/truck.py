class TruckAtCapacityError(ValueError):
    pass


class Truck:

    def __init__(self, truck_id=None, driver=None, location=None, speed=18, capacity=16):
        self._id = truck_id
        self._driver = driver
        self._location = location
        self._speed = speed
        self._capacity = capacity
        self._total_distance = 0
        self._size = 0
        self._undelivered = []
        self._delivered = []

    def __len__(self):
        return self._size

    def __contains__(self, item):
        if item in self._undelivered:
            return True
        return False

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
    def total_distance(self):
        return self._total_distance

    @total_distance.setter
    def total_distance(self, total_distance):
        self._total_distance = total_distance

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
        self._undelivered.append(package)
        self._size += 1

    def sort_undelivered_packages(self):
        """
        Sorts undelivered packages by their deadlines.
        This is so the higher priority ones are more easily accessible
        at the back of the truck.
        :return:
        """
        self._undelivered = sorted(self._undelivered, key=lambda package: package.deadline, reverse=True)
