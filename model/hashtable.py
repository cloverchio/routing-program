class HashTable:

    def __init__(self, capacity=100, load_factor=0.75):
        """
        Custom hashtable implementation.

        Relates to section E of the requirements.

        :param capacity: in which to initialize the hashtable with.
        :param load_factor: in which to initialize the hashtable with.
        """
        self._table = []
        self._capacity = capacity
        self._load_factor = load_factor
        self._size = 0
        for i in range(0, capacity):
            self._table.append([])

    def __len__(self):
        return self._size

    def __contains__(self, item):
        return self.get(item) is not None

    def __iter__(self):
        return iter(self._all_entries())

    def keys(self):
        """
        Used to retrieve all of the keys in the hashtable.
        :return: set of keys available in the hashtable.
        """
        return {entry[0] for entry in self._all_entries()}

    def values(self):
        """
        Used to retrieve all of the values in the hashtable.
        :return: list of values available in the hashtable.
        """
        return [entry[1] for entry in self._all_entries()]

    def get(self, key):
        """
        Retrieves the value associated with the key from the hashtable.
        :param key: in which to retrieve the value for.
        :return: value associated with the key.
        """
        bucket, bucket_index = self._bucket_entry(key)
        if bucket_index is not None:
            return bucket[bucket_index][1]
        return None

    def add(self, key, value):
        """
        Adds an entry to the hashtable for the given key/value pair.
        :param key: to associate the value with.
        :param value: in which to retrieve using the key.
        :return:
        """
        if not key:
            raise TypeError("key must not be none")
        self._increment_size()
        bucket, bucket_index = self._bucket_entry(key)
        bucket_value = (key, value)
        if bucket_index is not None:
            bucket[bucket_index] = bucket_value
        else:
            bucket.append(bucket_value)

    def remove(self, key):
        """
        Removes the entry associated with the key from the hashtable.
        :param key: in which to remove the entry for.
        :return:
        """
        bucket, bucket_index = self._bucket_entry(key)
        if bucket_index is not None:
            bucket.pop(bucket_index)
            self._decrement_size()

    def _hash(self, key):
        return hash(key) % len(self._table)

    def _increment_size(self):
        current_load_factor = (1.0 * self._size) / len(self._table)
        if current_load_factor > self._load_factor:
            self._rehash()
        self._size += 1

    def _decrement_size(self):
        self._size -= 1

    def _rehash(self):
        temp = self._table.copy()
        self._table.clear()
        self._size = 0
        for i in range(0, len(temp) * 2):
            self._table.append([])
        for bucket in temp:
            if bucket:
                for entry in bucket:
                    self.add(entry[0], entry[1])

    def _all_entries(self):
        entries = []
        for bucket in self._table:
            for entry in bucket:
                entries.append(entry)
        return entries

    def _bucket_entry(self, key):
        bucket_index = self._hash(key)
        bucket = self._table[bucket_index]
        if bucket:
            for i in range(0, len(bucket)):
                entry = bucket[i]
                if entry[0] == key:
                    return bucket, i
        return bucket, None
