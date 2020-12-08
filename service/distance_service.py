from model.graph import Graph
from model.location_distance import LocationDistance


class DistanceService:

    def __init__(self, location_data, distance_data):
        self._graph = Graph()
        self._location_data = location_data
        self._distance_data = distance_data
        # TODO implement graphing

    def _to_location_distances(self):
        location_distances = []
        for row_index in range(0, len(self._location_data)):
            location_row = self._location_data[row_index]
            distances = [float(distance) for distance in self._distance_data[row_index] if distance != '']
            location_distances.append(self._to_location_distance(location_row[0], location_row[1], distances))
        return location_distances

    @staticmethod
    def _to_location_distance(name, address, distances):
        location_distance = LocationDistance()
        location_distance.name = name
        location_distance.address = address
        location_distance.distances = distances
        return location_distance
