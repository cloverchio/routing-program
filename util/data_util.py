import csv


class DataUtil:

    def __init__(self):
        """
        Used for convenient access to the rows in the
        project's data files.
        """
        self._distance_data = []
        self._location_data = []
        self._package_data = []

    def distance_data(self):
        if not self._distance_data:
            self._distance_data.extend(self._load_data("wgups_distances.csv"))
        return self._distance_data

    def location_data(self):
        if not self._location_data:
            self._location_data.extend(self._load_data("wgups_locations.csv"))
        return self._location_data

    def package_data(self):
        if not self._package_data:
            self._package_data.extend(self._load_data("wgups_packages.csv"))
        return self._package_data

    @staticmethod
    def _load_data(file_path):
        data = []
        with open("data/" + file_path, 'r') as data_file:
            csv_reader = csv.reader(data_file)
            for row in csv_reader:
                data.append([val.strip() for val in row])
            data_file.close()
        return data
