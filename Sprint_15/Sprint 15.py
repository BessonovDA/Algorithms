# n = int(input())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))


# def getelement(i, arr):
#     return arr[i]

# result = []
# for i in range(0, n):
# 	result.append(getelement(i, arr1))
# 	result.append(getelement(i, arr2))
# print(" ".join(list(map(str, result))))

# # __________________________________________________

# n = int(input())
# qi = list(map(int, input().split()))
# k = int(input())
# result = []
# current_sum = sum(qi[0:k])
# result.append(current_sum / k)
# for i in range(0, n - k):
#     current_sum -= qi[i]
#     current_sum += qi[i + k]
#     result.append(current_sum / k)
# print(" ".join(list(map(str, result))))

# __________________________________________________
# Две фишки. Наивный алгоритм.

# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())

# result = []
# for i in range(0, n):
#     if len(result) == 0:
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == k:
#                 result.append((arr[i], arr[j]))
# if len(result) == 0:
#     print(None)
# else:
#     print(" ".join(list(map(str, result[0]))))

# # __________________________________________________
# # Две фишки. Вариант доп память.

# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())

# previous = set()
# result = []
# for i in range(0, n):
#     qj = k - arr[i]
#     if qj in previous:
#         result.append((arr[i], qj))
#     else:
#         previous.add(arr[i])
# if len(result) == 0:
#     print(None)
# else:
#     print(" ".join(list(map(str, result[0]))))

# # __________________________________________________
# # Две фишки. Вариант сортировка.

# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())

# arr.sort()
# left = 0
# right = n - 1
# result = []
# while left < right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == k:
#         result.append((arr[left], arr[right]))
#     if current_sum < k:
#         left += 1
#     else:
#         right -= 1
# if len(result) == 0:
#     print(None)
# else:
#     print(" ".join(list(map(str, result[0]))))

# __________________________________________________
# Поиск простого. Наивный алгоритм 1.

# def is_prime1(n):
#     if n == 1:
#         return False
#     i = 2
#     while i < n:
#         print(i)
#         if n % i == 0:
#             print(f'yes!! {i}')
#          #   return False
#         i = i + 1
#     return True

# # __________________________________________________
# # Поиск простого. Наивный алгоритм 2.


# def is_prime2(n):
#     if n == 1:
#         return False
#     i = 2
#     while i * i <= n:
#         print(i)
#         print(i * i)
#         print(n)
#         if n % i == 0:
#             print(f'yes!! {i}')
#          #   return False
#         i = i + 1
#     return True


# # print(is_prime1(20))
# print(is_prime2(29))


# __________________________________________________
# Задача: A. Значения функции
# arr = list(map(int, input().split()))
# print((arr[0] * arr[1] * arr[1]) + (arr[2] * arr[1]) + arr[3])

# __________________________________________________
# Задача: B.Чётные и нечётные числа

# input = '7 11 8'
# arr = list(map(int, input.split()))
# counter_ch = 0
# counter_no_ch = 0
# for num in arr:
#     if num % 2 == 0:
#         counter_ch += 1
#     else:
#         counter_no_ch += 1
# if counter_ch == 3 or counter_no_ch == 3:
#     print('WIN')
# else:
#     print('FAIL')

# __________________________________________________
# Задача: C. Соседи

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
#     m = int(context[1])
#     matrix = [
#         [int(num) for num in line.split(' ')] for line in context[2:n+2]
#     ]
#     x = int(context[n+2])
#     y = int(context[n+3])

# output = []
# for i in range(len(matrix)):
#     if i == x:
#         if y-1 >= 0:
#             output.append(matrix[i][y-1])
#         if y+1 < m:
#             output.append(matrix[i][y+1])
#     if (i == x-1 and x-1 >= 0) or (i == x+1 and x+1 <= n):
#         output.append(matrix[i][y])
# output.sort()
# print(" ".join(list(map(str, output))))

# # __________________________________________________
# Задача: D. Хаотичность погоды


# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
#     arr = list(map(int, context[1].split(' ')))
# output = []
# for i in range(len(arr)):
#     if n == 1:
#         output.append(arr[i])
#     else:
#         if i == 0 and arr[i] > arr[i+1]:
#             output.append(arr[i])
#         if i == n-1 and arr[i] > arr[i-1]:
#             output.append(arr[i])
#         if i != 0 and i != n-1 and arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#             output.append(arr[i])

# print(len(output))

# __________________________________________________
# Задача: E. Самое длинное слово. Вариант 1 (быстрее)

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     L = int(context[0])
#     arr = list(map(str, context[1].split(' ')))
#     arr = [line.rstrip() for line in arr]
# output = {}
# for i in range(len(arr)):
#     output[i] = len(arr[i])
# j = max(output, key=output.get)
# print(arr[j])
# print(len(arr[j]))

# __________________________________________________
# Задача: E. Самое длинное слово. Вариант 2 (медленней)

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     L = int(context[0])
#     arr = list(map(str, context[1].split(' ')))
#     arr = [line.rstrip() for line in arr]
# output = {}
# longer_word = ''

# for word in arr:
#     if len(word) > len(longer_word):
#         longer_word = word
# print(longer_word)
# print(len(longer_word))

# __________________________________________________
# Задача: F. Палиндром

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     arr = ''.join(context[0].split()).lower()
# for p in set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
#     if p in arr:
#         arr = arr.replace(p, '')
# result = True
# n = len(arr)
# for i in range(n // 2):
#     j = (n - 1) - i
#     if arr[i] != arr[j]:
#         result = False
# print(result)

# __________________________________________________
# Задача: G. Работа из дома
# (переводиv целое число из десятичной системы в двоичную.)
# base = 2
# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     x = int(context[0])
# output = ''
# if x != 0:
#     while x > 0:
#         output = str(x % base) + output
#         x //= base
#     print(output)
# else:
#     print(0)

# __________________________________________________
# Задача: H. Двоичная система

# x = [*map(int, input())]
# y = [*map(int, input())]

# x = x[::-1]
# y = y[::-1]

# size = max(len(x), len(y))
# x += [0] * (size - len(x))
# y += [0] * (size - len(y))
# overflow = 0
# res = []
# for obj in zip(x, y):

#     value = obj[0] + obj[1] + overflow
#     overflow = value // 2
#     res.append(value % 2)
# if overflow == 1:
#     res.append(1)
# res = res[::-1]
# print(''.join(map(str, res)))

# __________________________________________________
# Задача: I. Степень четырёх

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
# while n >= 1:
#     if n == 1:
#         print('True')
#         break
#     n = n / 4
# else:
#     print('False')

# __________________________________________________
# Задача: J. Факторизация

# def is_prime(n):
#     if n == 1:
#         return False
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True


# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
# output = []
# if is_prime(n):
#     output.append(n)
# else:
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             output.append(i)
#             n //= i
#             if is_prime(n):
#                 output.append(n)
#                 break
#         else:
#             i = i + 1
# print(' '.join(map(str, output)))


# __________________________________________________
# Задача: K. Списочная форма

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     len_x = int(context[0])
#     arr_x = list(map(int, context[1].split(' ')))
#     k = int(context[2])
# x = 0
# for i in range(len_x):
#     x += arr_x[i] * (10 ** ((len_x-1) - i))
# print(' '.join(str(k + x)))

# __________________________________________________
# Задача: L. Лишняя буква

# def compare_arrays(arr_short, arr_long):
#     for i in range(len(arr_short)):
#         arr_long.remove(arr_short[i])
#     print(str(arr_long[0]))


# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     arr_x = list(''.join(context[0].split()).rstrip())
#     arr_y = list(''.join(context[1].split()).rstrip())

# if len(arr_x) > len(arr_y):
#     compare_arrays(arr_short=arr_y, arr_long=arr_x)
# else:
#     compare_arrays(arr_short=arr_x, arr_long=arr_y)

# __________________________________________________
# Задача:  A. Ближайший ноль

# Тимофей ищет место, чтобы построить себе дом.
# Улица, на которой он хочет жить, имеет длину n, то есть состоит из n
# одинаковых идущих подряд участков. Каждый участок либо пустой, либо
# на нём уже построен дом. Общительный Тимофей не хочет жить далеко от
# других людей на этой улице. Поэтому ему важно для каждого участка
# знать расстояние до ближайшего пустого участка.
# Если участок пустой, эта величина будет равна нулю — расстояние до
# самого себя. Помогите Тимофею посчитать искомые расстояния. Для этого
# у вас есть карта улицы. Дома в городе Тимофея нумеровались в том
# порядке, в котором строились, поэтому их номера на карте никак не
# упорядочены. Пустые участки обозначены нулями.

# print('variant I----------------------------')

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
#     arr = list(map(int, context[1].split(' ')))

# index_null = []
# output = []
# for i in range(n):
#     if arr[i] == 0:
#         index_null.append(i)
# print('index_null =', index_null)
# for i in range(n):
#     print('____________')
#     print('i=', i)
#     print('arr_i=', arr[i])
#     if i in index_null:
#         output.append(0)
#         print('alrady 0')
#     else:
#         output.append(min([abs(i - j) for j in index_null]))
#         x_min = min([abs(i - j) for j in index_null])
#         x1 = [abs(i - j) for j in index_null]
#         print('x1=', x1)
#         print('x_min=', x_min)
# print(' '.join(map(str, output)))


# # __________________________________________________

# print('variant I A----------------------------')

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
#     arr = list(map(int, context[1].split(' ')))
# n = int(input())
# arr = list(map(int, input().split(' ')))

# index_null = []
# output = []
# for i in range(n):
#     if arr[i] == 0:
#         index_null.append(i)

# for i in range(n):
#     if i in index_null:
#         output.append(0)
#     else:
#         output.append(min([abs(i - j) for j in index_null]))
# print(' '.join(map(str, output)))


# __________________________________________________

# print('variant III----------------------------')

# Задача:  A. Ближайший ноль
# Успешная попытка 79998460 от 24 дек 2022, 16:45:39

# with open('input.txt', 'r') as f:
#     context = f.readlines()
#     n = int(context[0])
#     arr = list(map(int, context[1].split(' ')))

# index_null = []
# output = []
# for i in range(n):
#     if arr[i] == 0:
#         index_null.append(i)


# def symmetric_range(arr_len):
#     arr = [0] * arr_len
#     left = 0
#     right = arr_len-1
#     i = 1
#     while left <= right:
#         arr[left] = i
#         arr[right] = i
#         left += 1
#         right -= 1
#         i += 1
#     return arr


# def unsymmetric_range_begin(arr_len):
#     arr = [0] * arr_len
#     left = 0
#     right = arr_len-1
#     i = 1
#     while left <= right:
#         arr[right] = i
#         right -= 1
#         i += 1
#     return arr


# def unsymmetric_range_end(arr_len):
#     arr = [0] * arr_len
#     left = 0
#     right = arr_len-1
#     i = 1
#     while left <= right:
#         arr[left] = i
#         left += 1
#         i += 1
#     return arr


# for j in range(0, len(index_null)+1):
#     if j == 0:
#         output += unsymmetric_range_begin(index_null[j])
#         output.append(0)
#     else:
#         if j == len(index_null):
#             output += unsymmetric_range_end(n - index_null[j-1] - 1)
#         else:
#             output += symmetric_range(index_null[j] - index_null[j-1] - 1)
#             output.append(0)
# print(' '.join(map(str, output)))

# __________________________________________________
# Задача: B. Ловкость рук
# Успешная попытка 80001820 от 24 дек 2022, 17:58:27

with open('input.txt', 'r') as f:
    context = f.readlines()
    k = int(context[0])
    str_arr = []
    for line in context[1:5]:
        str_arr += line.rstrip().replace('.', '')
matrix = list(map(int, str_arr))
dict = {}
for i in set(matrix):
    dict[i] = matrix.count(i)

result = 0
for t in range(0, 10):
    if dict.get(t):

        if dict.get(t) <= k*2:
            result += 1
print(result)
