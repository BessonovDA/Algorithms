def fibonacci_num(number):
    print(number)
    if number == 0 or number == 1:
        return 1
    result = fibonacci_num(number - 1) + fibonacci_num(number - 2)
    return result


if __name__ == '__main__':
    print('result', fibonacci_num(int(input())))
