
class LocationDistance:

    def __init__(self, name=None, address=None, distances=None):
        self._name = name
        self._address = address
        self._distances = distances

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances

