def fibonacci_num(number):
    result = 0
    prev_i_1 = 1
    prev_i_2 = 1
    index = 0
    while index < number - 1:
        result = prev_i_1 + prev_i_2
        prev_i_2 = prev_i_1
        prev_i_1 = result
        index += 1

    return result


if __name__ == '__main__':
    input = input().split(' ')
    print(fibonacci_num(int(input[0])) % 10 ** int(input[1]))
