# E. Develop a hash table, without using any additional libraries or classes.
class HashTable:

    def __init__(self, capacity=100, load_factor=0.75):
        self.table = []
        self.load_factor = load_factor
        self.size = 0
        for i in range(0, capacity):
            self.table.append([])

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return self.get(item) is not None

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
                    return

    def _hash(self, key):
        return hash(key) % len(self.table)

    def _increment_size(self):
        current_load_factor = (1.0 * self.size) / len(self.table)
        if current_load_factor > self.load_factor:
            self._rehash()
        self.size += 1

    def _decrement_size(self):
        self.size -= 1

    def _rehash(self):
        temp = self.table.copy()
        self.table.clear()
        self.size = 0
        for i in range(0, len(temp) * 2):
            self.table.append([])
        for bucket in temp:
            if bucket:
                for entry in bucket:
                    self.add(entry[0], entry[1])
