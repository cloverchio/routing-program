import math


class HashTable:

    def __init__(self, capacity=100, load_factor=0.75):
        self.table = []
        self.load_factor = load_factor
        self.size = 0
        for i in range(0, capacity):
            self.table.append([])

    def __len__(self):
        return self.size

    def get(self, key):
        """
        Retrieves the value associated with the key from the hashtable.
        :param key: in which to retrieve the value for.
        :return: value associated with the key.
        """
        bucket_index = self._hash(key)
        bucket = self.table[bucket_index]
        if bucket:
            for entry in bucket:
                if entry[0] == key:
                    return entry[1]
        return None

    def add(self, key, value):
        """
        Adds an entry to the hashtable using the given key/value pair.
        :param key: to associate the value with.
        :param value: in which to retrieve using the key.
        :return:
        """
        if not key:
            raise TypeError("key must not be none")
        self._increment_size()
        bucket_index = self._hash(key)
        bucket_value = (key, value)
        bucket = self.table[bucket_index]
        if bucket is None:
            self.table[bucket_index] = list(bucket_value)
        else:
            for i in range(0, len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = bucket_value
                    return
            bucket.append(bucket_value)

    def remove(self, key):
        """
        Removes the entry associated with the key from the hashtable.
        :param key: in which to remove the entry for.
        :return:
        """
        bucket_index = self._hash(key)
        bucket = self.table[bucket_index]
        if bucket:
            for i in range(0, len(bucket)):
                if bucket[i][0] == key:
                    bucket.pop(i)
                    self._decrement_size()

    def _hash(self, key):
        return hash(key) % len(self.table)

    def _increment_size(self):
        # resize if threshold is violated
        if self.size + 1 >= math.ceil(len(self.table) * self.load_factor):
            self._resize()
        self.size += 1

    def _decrement_size(self):
        self.size -= 1

    def _resize(self):
        table_len = len(self.table)
        temp = [None] * (table_len * 2)
        for i in range(0, table_len):
            temp[i] = self.table[i]
        self.table = temp
