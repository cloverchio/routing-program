from datetime import timedelta

from model.hashtable import HashTable
from model.truck import Truck
from service.delivery_service import DeliveryService
from util.data_util import DataUtil as Data


class TrackingService:

    def __init__(self):
        data = Data()
        # caching time based queries to avoid having to lookup
        # subsequent requests for the same time
        self._time_status_cache = HashTable()
        self._delivery_service = DeliveryService("4001 South 700 East",
                                                 data.location_data(),
                                                 data.distance_data(),
                                                 data.package_data())
        # define trucks
        trucks = [Truck(1, 1), Truck(2, 2), Truck(3, 3)]
        # load and deliver packages
        self._delivery_service.load_packages(trucks)
        self._delivery_service.deliver_packages(trucks)

    def status_by_package_id(self, package_id):
        """
        Retrieves a string representation of the package status.

        Relates to section F of the requirements.

        :param package_id: in which to retrieve the status for.
        :return: status to be displayed in the console for given package id.
        """
        return self._delivery_service.package_status(int(package_id))

    def status_by_time(self, time_str):
        """
        Retrieves the status for all of the packages within the given timeframe.

        Relates to section G of the requirements.

        :param time_str: the timeframe in which to lookup the package statuses.
        :return: statuses to be displayed in the console for the given timeframe.
        """
        hours, minutes, seconds = time_str.split(':')
        time = timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        if time in self._time_status_cache.keys():
            return self._time_status_cache.get(time)
        status = self._delivery_service.package_status_by_time(time)
        self._time_status_cache.add(time, status)
        return status

    def mileage(self):
        """
        Retrieves a string representation of the total mileage
        of the delivery. The sum of miles across all trucks.

        Relates to section G of the requirements.

        :return: the sum of miles across all trucks.
        """
        return str(self._delivery_service.total_mileage())
