def left_bound(list_a, key):
    left = -1
    right = len(list_a)
    while right - left > 1:
        middle = (left + right) // 2
        if list_a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(list_a, key):
    left = -1
    right = len(list_a)
    while right - left > 1:
        middle = (left + right) // 2
        if list_a[middle] <= key:
            left = middle
        else:
            right = middle
    return right


if __name__ == '__main__':
    list_x = [2, 2, 4, 5, 8, 9, 10, 11, 15]
    print(left_bound(list_x, 6))
    print(right_bound(list_x, 6))
