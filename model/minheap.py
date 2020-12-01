from typing import Tuple


class MinHeap:

    def __init__(self, capacity=100):
        self.size = 0
        self.capacity = capacity
        self.heap = [(0.0, None)] * (capacity + 1)
        self.heap[0] = (-1 * float('inf'), None)
        self.head_position = 1

    def __len__(self):
        return self.size

    def push(self, element: Tuple[float, any]):
        """
        Pushes the given element onto the heap.
        If you did not bring a tuple one will be provided for you...
        :param element: to be added to the heap.
        :return:
        """
        if type(element) is not tuple:
            element = (element, None)
        self._increment_size()
        self.heap[self.size] = element
        current_position = self.size
        parent_position = self._parent(current_position)
        while self.heap[current_position][0] < self.heap[parent_position][0]:
            self._swap(current_position, parent_position)
            current_position = parent_position

    def pop(self):
        """
        Pops the smallest element from the heap in the form of a tuple.
        :return: the smallest element from the heap.
        """
        if self.size == 0:
            raise ValueError("heap is empty")
        min_element = self.heap[self.head_position]
        self.heap[self.head_position] = self.heap[self.size]
        self._decrement_size()
        self.min_heapify(self.head_position)
        return min_element

    def min_heapify(self, position):
        """
        Performs the heapify operation at a given position.
        Responsible for maintaining the ordering of elements on the heap.
        :param position: in which to perform the heapify operation on.
        :return:
        """
        if not self._leaf(position) and self.size > 0:
            left_position = self._left(position)
            right_position = self._right(position)
            current = self.heap[position]
            left = self.heap[left_position]
            right = self.heap[right_position]
            if current > left or current > right:
                if left < right:
                    self._swap(position, left_position)
                    self.min_heapify(left_position)
                else:
                    self._swap(position, right_position)
                    self.min_heapify(right_position)

    def min_heap(self):
        """
        Used to reconstruct the entire heap.
        :return:
        """
        for position in range(self.size // 2, 0, -1):
            self.min_heapify(position)

    def _increment_size(self):
        if self.size + 1 > self.capacity:
            self._resize()
        self.size += 1

    def _decrement_size(self):
        self.size -= 1

    def _resize(self):
        temp = [None] * ((self.size * 2) + 1)
        for i in range(0, len(self.heap)):
            temp[i] = self.heap[i]
        self.heap = temp

    def _leaf(self, position):
        return (self.size // 2) <= position <= self.size

    def _swap(self, first_position, second_position):
        temp = self.heap[first_position]
        self.heap[first_position] = self.heap[second_position]
        self.heap[second_position] = temp

    @staticmethod
    def _parent(position):
        return position // 2

    @staticmethod
    def _left(position):
        return position * 2

    @staticmethod
    def _right(position):
        return (position * 2) + 1
