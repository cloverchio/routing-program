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
                 en_route_time=None,
                 delivery_time=None,
                 status=DeliveryStatus.HUB,
                 priority=Priority.LOW):
        self._id = package_id
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip_code
        self._deadline = deadline
        self._weight = weight
        self._en_route_time = en_route_time
        self._delivery_time = delivery_time
        self._note = note
        self._status = status
        self._priority = priority

    def __str__(self):
        return self._str_format(self._status, self._delivery_time)

    def status_by_time(self, time):
        if self._delivery_time <= time:
            return str(self)
        if self._en_route_time <= time < self._delivery_time:
            return self._str_format(DeliveryStatus.EN_ROUTE.value, None)
        return self._str_format(DeliveryStatus.HUB.value, None)

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
    def en_route_time(self):
        return self._en_route_time

    @en_route_time.setter
    def en_route_time(self, en_route_time):
        self._en_route_time = en_route_time

    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, delivery_time):
        self._delivery_time = delivery_time

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

    def _str_format(self, status, delivery_time):
        return "Package Id: {}, " \
               "Address: {}, " \
               "City: {}, " \
               "Zip: {}, " \
               "Weight: {}, " \
               "Deadline: {}, " \
               "Status: {}, " \
               "Time Delivered: {}" \
            .format(self._id,
                    self._address,
                    self._city,
                    self._zip,
                    self._weight,
                    self._deadline,
                    status,
                    delivery_time)
