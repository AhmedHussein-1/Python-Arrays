class Empty(Exception):
    pass

class Stack(object):
    """Array based LIFO Stack data structure."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data.pop()


if __name__ == "__main__":
    pass
    S = Stack()
    S.push("A")
    S.push(2)
    S.push(8)
    S.push(14)
    S.push(61)
    S.push(13)
    S.pop()
    print(len(S))

    #This will pop all of the element in stack S
    for i in range(len(S)):
        S.pop()
    print(len(S))