from model.package import Package
from model.hashtable import HashTable


class PackagingService:

    def __init__(self, package_data):
        """
        Responsible for managing package data.
        :param package_data: to be managed and transformed.
        """
        self._package_cache = HashTable()
        self._load_package_cache(package_data)

    def get_packages(self, package_ids):
        """
        Retrieve data for multiple package ids.
        :param package_ids: in which to retrieve package data for.
        :return: list of package objects associated with the ids.
        """
        return [self.get_package(package_id) for package_id in package_ids]

    def get_package(self, package_id):
        """
        Retrieve package data by a given package id.
        :param package_id: in which to retrieve package data for.
        :return: the package object associated with the id.
        """
        return self._package_cache.get(package_id)

    def get_all_package_ids(self):
        """
        Retrieves a set of all package ids.
        :return: set of all package ids.
        """
        return self._package_cache.keys()

    def get_all_packages(self):
        """
        Retrieves a list of all packages.
        :return: list of all packages.
        """
        return self._package_cache.values()

    def _load_package_cache(self, package_data):
        for row in package_data:
            package = self._to_package(row)
            self._package_cache.add(package.id, package)

    @staticmethod
    def _to_package(package_data_row):
        package = Package()
        package.id = int(package_data_row[0])
        package.address = package_data_row[1]
        package.city = package_data_row[2]
        package.zip = package_data_row[4]
        package.deadline = package_data_row[5]
        package.weight = package_data_row[6]
        note = package_data_row[7]
        if note != '':
            package.note = note
        return package
