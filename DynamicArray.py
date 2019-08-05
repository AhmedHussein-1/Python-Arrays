import ctypes


class DynamicArray(object):
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = (self._capacity * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __setitem__(self, index, value):
        if not 0 <= index < self._n:
            raise IndexError("invalid index")
        self._A[index] = value

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError("invalid index")
        return self._A[index]

    # Grow the array dynamically
    def _resize(self, c):
        B = (c * ctypes.py_object)()
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self, obj):
        if self._n == self._capacity:  # dynamic array is full
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    # Remove the last element of the array
    def pop(self, index):
        if self._n > 1:
            self._A[self._n - 1] = None  # setting the last element to None
            # will be interpreted as not having an element at all
            self._n -= 1
            # remove works by deleting the first occurrence of obj
            # and shifting all element to the left
            for k in range(self._n, index):
                if self._A[k] == obj:
                    for j in range(k, self._n - 1):
                        self._A[j] = self._A[j + 1]
                    self._A[self._n - 1] = None
                    self._n -= 1
                    return
            #raise ValueError('Value not found')


        # Shrink the capacity of the array by half any time the number of elements in the
        # array is below 1/4
        if self._n <= self._capacity / 4:
            self._resize(self._capacity // 2)

    def insert(self, k, obj):
        if self._n == self._capacity:  # dynamic array is full
            self._resize(2 * self._capacity)

        # we need to shift elements
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]

        self._A[k] = obj
        self._n += 1


if __name__ == "__main__":
    L = DynamicArray()
    # TEST pop(k) HERE

    L.append(1)
    L.append(1)
    L.append(1)
    L.append(1)
    L.append(1)
    L.append(1)
    L.append(1)
    L.append(1)
    L.pop(2)
    print(len(L))