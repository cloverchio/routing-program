class Package:

    def __init__(self, id, address, city, zip, deadline, weight, state='UT', note=None, delivered=False):
        self._id = id
        self._address = address
        self._city = city
        self._state = state
        self._zip = zip
        self._deadline = deadline
        self._weight = weight
        self._note = note
        self._delivered = delivered

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def zip(self, zip):
        self._zip = zip

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
    def delivered(self):
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        self._delivered = delivered
