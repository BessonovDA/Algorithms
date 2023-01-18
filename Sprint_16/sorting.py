def merge(list_a: list, list_b: list):
    result = [0] * (len(list_a) + len(list_b))
    index_a = index_b = index_result = 0
    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] <= list_b[index_b]:
            result[index_result] = list_a[index_a]
            index_a += 1
            index_result += 1
        else:
            result[index_result] = list_b[index_b]
            index_b += 1
            index_result += 1
    while index_a < len(list_a):
        result[index_result] = list_a[index_a]
        index_a += 1
        index_result += 1
    while index_b < len(list_b):
        result[index_result] = list_b[index_b]
        index_b += 1
        index_result += 1
    return result


def sort_merge(list_a: list):
    if len(list_a) <= 1:
        return list_a
    middle = len(list_a) // 2
    list_left = [list_a[index] for index in range(middle)]
    list_right = [list_a[index] for index in range(middle, len(list_a))]
    return merge(sort_merge(list_left), sort_merge(list_right))


def sort_hoar(list_a):
    if len(list_a) <= 1:
        return list_a
    barrier = list_a[0]
    list_left = []
    list_middle = []
    list_right = []
    for obj in list_a:
        if obj < barrier:
            list_left.append(obj)
        elif obj == barrier:
            list_middle.append(obj)
        else:
            list_right.append(obj)
    return sort_hoar(list_left) + list_middle + sort_hoar(list_right)


def check_sorted(list_a, ascending=True):
    """ Проверка отсортированности за О(len(list_a)) """
    flag = True
    sort_order = 2 * int(ascending) - 1
    for index in range(0, len(list_a)-1):
        if sort_order * list_a[index] > sort_order * list_a[index + 1]:
            flag = False
            break
    return flag


if __name__ == '__main__':
    list_x = [11, 5, 9, 2, 2, 4, 8, 10, 15]
    print(sort_merge(list_x))
    print(sort_hoar(list_x))
    print(check_sorted(list_x))
    print(check_sorted(sort_hoar(list_x)))
