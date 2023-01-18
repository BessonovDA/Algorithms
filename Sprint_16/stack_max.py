class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return None
        max_item = self.items[0]
        for item in self.items:
            if item > max_item:
                max_item = item
        return max_item


if __name__ == '__main__':
    new_stack = StackMax()
    n = int(input())
    while(n):
        command = input().split()
        if command[0] == 'push':
            new_stack.push(int(command[1]))
        elif command[0] == 'get_max':
            print(new_stack.get_max())
        elif command[0] == 'pop':
            result = new_stack.pop()
            if result == 'error':
                print(result)
        n -= 1
