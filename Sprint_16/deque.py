# Задача:  A. Дек
# Успешная попытка 81363824 от 25 янв 2023, 19:21:11


DEQUE_OVERFLOW_MESSAGE = 'Deque exceeded max size'
DEQUE_EMPTY_MESSAGE = 'Deque is empty'
METHOD_NOT_FOUND = 'Method {method} not found'


class Deque:
    def __init__(self, max_size):
        self.cells = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_front(self, new_item):
        if self.size == self.max_size:
            raise IndexError(DEQUE_OVERFLOW_MESSAGE)
        self.head = (self.head - 1) % self.max_size
        self.cells[self.head] = new_item
        self.size += 1

    def push_back(self, new_item):
        if self.size == self.max_size:
            raise IndexError(DEQUE_OVERFLOW_MESSAGE)
        self.tail = (self.tail + 1) % self.max_size
        self.cells[self.tail] = new_item
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError(DEQUE_EMPTY_MESSAGE)
        item = self.cells[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError(DEQUE_EMPTY_MESSAGE)
        item = self.cells[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    commands_count = int(input())
    deque = Deque(int(input()))
    for _ in range(commands_count):
        method, *parameters = input().split()
        try:
            result = getattr(deque, method)(*parameters)
            if result is not None:
                print(result)
        except AttributeError:
            raise ValueError(METHOD_NOT_FOUND.format(method=method))
        except IndexError:
            print('error')
