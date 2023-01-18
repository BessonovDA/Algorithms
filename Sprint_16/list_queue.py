class MyListQueue:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.head = 0
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def get(self):
        if self.is_empty:
            return 'error'
        else:
            item = self.head
            return item


    def put(self, item):
        pass

    def size(self):
        return self.queue_size


if __name__ == '__main__':
    n = int(input())
    new_queue = MyListQueue()
    while(n):
        command = input().split()
        if command[0] == 'put':
            new_queue.put(command[1])
        elif command[0] == 'size':
            print(new_queue.size())
        elif command[0] == 'get':
            print(new_queue.get())
        n -= 1
