import math


class HashTable:

    def __init__(self, capacity=100, load_factor=0.75):
        self.table = []
        self.load_factor = load_factor
        self.size = 0
        for i in range(0, capacity):
            self.table[i] = []

    def __len__(self):
        return self.size

    def insert(self, key, value):
        self._increment_size()
        bucket_index = self._hash(key)
        bucket_value = (key, value)
        bucket = self.table[bucket_index]
        if bucket is None:
            self.table[bucket_index] = list(bucket_value)
            return value
        else:
            for i in range(0, len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = bucket_value
                    return value
            self.table[bucket_index].append(bucket_value)
            return value

    def _hash(self, key):
        return hash(key) % len(self.table)

    def _increment_size(self):
        threshold = math.ceil(len(self.table) / self.load_factor)
        if self.size + 1 > threshold:
            self._resize()
        self.size += 1

    def _resize(self):
        table_len = len(self.table)
        temp = [None] * (table_len * 2)
        for i in range(0, table_len):
            temp[i] = self.table[i]
        self.table = temp
