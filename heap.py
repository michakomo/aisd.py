import sys


class MaxHeap:
    def __init__(self):
        self._items = [sys.maxsize]

    def __repr__(self):
        return str(self._items[1:])

    def insert(self, value):
        self._items.append(value)

        def _up_heap(i):
            tmp = self._items[i]

            while self._items[i >> 1] < tmp and i != 0:
                self._items[i] = self._items[i >> 1]
                i = i >> 1

            self._items[i] = tmp

        _up_heap(len(self._items) - 1)

    def delete_max(self):
        tmp = self._items[1]

        self._items[1] = self._items.pop()

        def _down_heap():
            n = len(self._items) - 1
            i = 1

            while True:
                if i << 1 > n:
                    break

                k = i << 1

                if i << 1 + 1 <= n and self._items[i << 1 + 1] > self._items[i << 1]:
                    k = i << 1 + 1

                if self._items[k] <= self._items[i]:
                    break

                self._items[i], self._items[k] = self._items[k], self._items[i]
                i = k

        _down_heap()
        return tmp
