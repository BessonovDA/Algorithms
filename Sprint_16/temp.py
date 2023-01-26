# Задача: B. Калькулятор
# Успешная попытка 81307301 от 24 янв 2023, 16:04:29


STACK_EMPTY_MESSAGE = 'Stack is empty'
UNEXPECTED_OPERAND_TYPE = 'Unexpected operand type'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('error')


def summation(operand_left, operand_right):
    return operand_left + operand_right


def subtraction(operand_left, operand_right):
    return operand_left - operand_right


def division_by_modulus(operand_left, operand_right):
    return operand_left // operand_right


def multiplication(operand_left, operand_right):
    return operand_left * operand_right


def calculator(expressions, stack=None, operand_type=int):
    stack = Stack() if stack is None else stack
    for token in expressions:
        if token in ['+', '-', '*', '/']:
            right, left = stack.pop(), stack.pop()
            if token == '+':
                calculation_function = summation
            if token == '-':
                calculation_function = subtraction
            if token == '*':
                calculation_function = multiplication
            if token == '/':
                calculation_function = division_by_modulus
            stack.push(calculation_function(left, right))
        else:
            operand = 0
            try:
                operand = operand_type(token)
            except ValueError:
                print(UNEXPECTED_OPERAND_TYPE)
            stack.push(operand)
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split(' ')))
