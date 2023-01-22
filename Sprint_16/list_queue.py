class QueueNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def is_empty(self):
        return self.size() == 0

    def get(self):
        if self.is_empty():
            return 'error'
        else:
            head = self.next
            self.next = head.next
            head.next = None
            return head.value

    def put(self, item):
        new_node = QueueNode(value=item)
        last_node = self
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def size(self):
        queue_size = 0
        last_node = self
        while last_node.next:
            last_node = last_node.next
            queue_size += 1
        return queue_size


if __name__ == '__main__':
    n = int(input())
    new_queue = QueueNode()
    while(n):
        command = input().split()
        if command[0] == 'put':
            new_queue.put(command[1])
        elif command[0] == 'size':
            print(new_queue.size())
        elif command[0] == 'get':
            print(new_queue.get())
        n -= 1
