from typing import Tuple


class MinHeap:

    def __init__(self):
        self.size = 0
        self.head_position = 1
        self.heap = [((-1.0 * float('inf')), None)]

    def push(self, element: Tuple[int, any]):
        """
        Pushes a given element onto the heap.
        If you did not bring a tuple, one will be provided for you...
        :param element: in which to add to the heap.
        :return:
        """
        if element is not type(tuple):
            element = (element, None)
        self.heap.append(element)
        self.size += 1
        self._sift_up(self.size)

    def pop(self):
        """
        Pops the minimum element from the heap.
        :return: the smallest element from the heap.
        """
        if len(self.heap) == 1:
            raise ValueError("heap is empty")
        min_element = self.heap[self.head_position]
        self.heap[self.head_position] = self.heap[self.size]
        self.heap.pop(self.head_position)
        self.size -= 1
        self._sift_down(self.head_position)
        return min_element

    def _sift_up(self, position):
        parent_position = self._parent(position)
        while parent_position:
            if self.heap[position] < self.heap[parent_position]:
                self._swap(position, parent_position)
            parent_position = parent_position // 2

    def _sift_down(self, position):
        while self._left(position) <= self.size:
            min_position = self._min_position(position)
            if self.heap[position] > self.heap[min_position]:
                self._swap(position, min_position)
            position = min_position

    def _min_position(self, position):
        right_position = self._right(position)
        left_position = self._left(position)
        if right_position > self.size:
            return left_position
        if self.heap[left_position] < self.heap[right_position]:
            return left_position
        return right_position

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
