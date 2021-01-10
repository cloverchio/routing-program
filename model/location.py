class Location:

    def __init__(self, name=None, address=None, distances=None):
        self._name = name
        self._address = address
        self._distances = distances

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def distances(self):
        return self._distances
