from model.package import Package
from model.hashtable import HashTable


class PackagingService:

    def __init__(self, package_data):
        """
        Responsible for managing the package data.
        :param package_data: to be managed and transformed
        by the service.
        """
        self._package_cache = HashTable()
        self._load_package_cache(package_data)

    def package(self, package_id):
        return self._package_cache.get(package_id)

    def _load_package_cache(self, package_data):
        for row in package_data:
            package = self._to_package(row)
            self._package_cache.add(package.id, package)

    @staticmethod
    def _to_package(package_data_row):
        package = Package()
        package.id = package_data_row[0]
        package.address = package_data_row[1]
        package.city = package_data_row[2]
        package.zip = package_data_row[4]
        package.deadline = package_data_row[5]
        package.weight = package_data_row[6]
        note = package_data_row[7]
        if note != '':
            package.note = note
        return package
