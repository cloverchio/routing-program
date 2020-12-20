class Delivery:

    def __init__(self, package_id=None, address=None, distance=None):
        self._package_id = package_id
        self._address = address
        self._distance = distance

    @property
    def package_id(self):
        return self._package_id

    @property
    def address(self):
        return self._address

    @property
    def distance(self):
        return self._distance
