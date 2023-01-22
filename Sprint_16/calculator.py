# Задача: B. Калькулятор
# Успешная попытка 81182761 от 22 янв 2023, 18:11:58


MATH_OPERATIONS = ['+', '-', '*', '/']


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return self.items.pop()


def calculator(expression):
    stack = Stack()
    for token in expression:
        if token not in MATH_OPERATIONS:
            stack.push(token)
        else:
            operand_right = stack.pop()
            operand_left = stack.pop()
            token = '//' if token == '/' else token
            stack.push(eval(f'{operand_left} {token} {operand_right}'))
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split(' ')))
