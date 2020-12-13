from enum import Enum


class Priority(Enum):
    HIGH = 'High'
    LOW = 'Low'


class DeliveryStatus(Enum):
    DELIVERED = 'Delivered'
    EN_ROUTE = 'En Route'
    HUB = 'At Hub'


class Package:

    def __init__(self, package_id=None,
                 address=None,
                 city=None,
                 zip_code=None,
                 deadline=None,
                 weight=None,
                 state='UT',
                 note=None,
                 status=DeliveryStatus.HUB,
                 priority=Priority.LOW):
        self._id = package_id
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip_code
        self._deadline = deadline
        self._weight = weight
        self._note = note
        self._status = status
        self._priority = priority

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, package_id):
        self._id = package_id

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, zip_code):
        self._zip = zip_code

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        self._deadline = deadline

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        self._note = note

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority
