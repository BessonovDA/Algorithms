class MyQueueSized:
    def __init__(self, queue_max):
        self.queue = [None] * queue_max
        self.max_len = queue_max
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def push(self, item):
        if self.queue_size != self.max_len:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_len
            self.queue_size += 1
            return item
        else:
            return

    def pop(self):
        if self.is_empty():
            return
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_len
        self.queue_size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return
        return self.queue[self.head]

    def size(self):
        return self.queue_size


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    new_queue = MyQueueSized(max_size)
    while(n):
        command = input().split()
        if command[0] == 'push':
            result = new_queue.push(command[1])
            if not result:
                print('error')
        elif command[0] == 'size':
            print(new_queue.size())
        elif command[0] == 'peek':
            print(new_queue.peek())
        elif command[0] == 'pop':
            print(new_queue.pop())
        n -= 1
