# Задача:  A. Дек
# Успешная попытка 81185652 от 22 янв 2023, 19:18:28


class Deque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_front(self, new_item):
        if self.size == self.max_size:
            return 'exceeded max size'
        self.head = (self.head - 1) % self.max_size
        self.deque[self.head] = new_item
        self.size += 1

    def push_back(self, new_item):
        if self.size == self.max_size:
            return 'exceeded max size'
        self.deque[self.tail] = new_item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            return 'error'
        item = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            return 'error'
        item = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    commands_count = int(input())
    test_deque = Deque(int(input()))
    while(commands_count):
        command = input().split()
        if command[0] == 'push_front':
            if test_deque.push_front(command[1]) == 'exceeded max size':
                print('error')
        elif command[0] == 'push_back':
            if test_deque.push_back(command[1]) == 'exceeded max size':
                print('error')
        elif command[0] == 'pop_back':
            print(test_deque.pop_back())
        elif command[0] == 'pop_front':
            print(test_deque.pop_front())
        commands_count -= 1
