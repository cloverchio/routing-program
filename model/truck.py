from datetime import timedelta

from model.package import DeliveryStatus


class TruckAtCapacityError(ValueError):
    pass


class TruckEmptyError(ValueError):
    pass


class Truck:

    def __init__(self,
                 truck_id=None,
                 driver=None,
                 location=None,
                 start_time=None,
                 current_time=None,
                 speed=18,
                 capacity=16,
                 packaging_service=None):
        self._id = truck_id
        self._driver = driver
        self._location = location
        self._start_time = start_time
        self._current_time = current_time
        self._speed = speed
        self._capacity = capacity
        self._packaging_service = packaging_service
        self._package_ids = []
        self._mileage = 0
        self._size = 0

    def __len__(self):
        return self._size

    def assigned_packages(self):
        return self._package_ids

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
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        if self._start_time is None:
            self._start_time = current_time
        self._current_time = current_time

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
    def packaging_service(self):
        return self._packaging_service

    @packaging_service.setter
    def packaging_service(self, packaging_service):
        self._packaging_service = packaging_service

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

    def add_packages(self, package_ids):
        """
        Assigns multiple package ids to the truck for delivery.
        :param package_ids: to be assigned to the truck.
        :return:
        """
        for package_id in package_ids:
            self.add_package(package_id)

    def add_package(self, package_id):
        """
        Assigns the given package id to the truck for delivery
        and updates the delivery status of the corresponding package.
        :param package_id: to be assigned to the truck.
        :return:
        """
        if self._size + 1 > self._capacity:
            raise TruckAtCapacityError("truck is at capacity")
        self._size += 1
        self._package_ids.append(package_id)
        package = self._packaging_service.get_package(package_id)
        package.status = DeliveryStatus.EN_ROUTE
        self._packaging_service.update_package(package)

    def deliver_package(self, package_id, distance):
        """
        Sets the truck's location to the delivery address, updates the mileage,
        and sets the delivery status of the package to delivered.
        Size of the truck is then decremented.
        :param package_id:
        :param distance:
        :return:
        """
        self._deliver_package(package_id, distance)

    def return_to_starting_location(self, starting_location, distance):
        """
        Represents the truck traveling to its original location (the hub for example).
        Sets the truck location to the starting location and updates the distance.
        :param starting_location: the location in which delivery started from.
        :param distance: to the starting location from the truck's current location.
        :return:
        """
        self._mileage += distance
        self._location = starting_location
        self._current_time += self._travel_time(distance)

    def _deliver_package(self, package_id, distance):
        if self._size == 0:
            raise TruckEmptyError("truck is empty")
        package = self._packaging_service.get_package(package_id)
        self._size -= 1
        self._mileage += distance
        self._location = package.address
        self._current_time += self._travel_time(distance)
        package.status = DeliveryStatus.DELIVERED
        package.en_route_time = self._start_time
        package.delivery_time = self._current_time
        self._packaging_service.update_package(package)

    def _travel_time(self, distance):
        return timedelta(hours=distance / self._speed)
