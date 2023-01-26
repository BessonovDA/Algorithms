# Задача: B. Калькулятор
# Успешная попытка 81363509 от 25 янв 2023, 19:16:20


import operator

STACK_EMPTY_MESSAGE = 'Stack is empty'
UNEXPECTED_OPERAND_TYPE = 'Unexpected operand type {token}'
CALCULATION_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv,
    '*': operator.mul
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError(STACK_EMPTY_MESSAGE)


def calculator(expressions, stack=None,
               allowed_operations=CALCULATION_OPERATIONS,
               operand_type=int):
    stack = Stack() if stack is None else stack
    for token in expressions:
        if token in allowed_operations:
            right, left = stack.pop(), stack.pop()
            stack.push(allowed_operations[token](left, right))
            continue
        try:
            stack.push(operand_type(token))
        except ValueError:
            raise ValueError(
                UNEXPECTED_OPERAND_TYPE.format(token=token)
            )
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split(' ')))
