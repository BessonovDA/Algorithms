
def reversal_of_matrix(matrix):
    return [list(index) for index in zip(*matrix)]


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        context = f.readlines()
        rows = int(context[0])
        columns = int(context[1])
        matrix = [
            [int(num) for num in line.split(' ')] for line in context[2:rows+2]
        ]
    for line in reversal_of_matrix(matrix):
        print(*line)
