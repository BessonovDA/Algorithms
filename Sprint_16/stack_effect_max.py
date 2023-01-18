class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(
            item if len(self.items) == 0 or item > self.items[-1]
            else self.items[-1])

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]


if __name__ == '__main__':
    new_stack = StackMaxEffective()
    n = int(input())
    while(n):
        command = input().split()
        if command[0] == 'push':
            new_stack.push(command[1])
        elif command[0] == 'get_max':
            print(new_stack.get_max())
        elif command[0] == 'pop':
            result = new_stack.pop()
            if result == 'error':
                print(result)
        n -= 1
