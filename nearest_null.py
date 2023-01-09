# Задача:  A. Ближайший ноль
# Успешная попытка 80130892 от 28 дек 2022, 18:23:44

def distances_to_symbol(symbols, target='0'):
    distances = [0] * len(symbols)
    zeros = [symbol_pos for symbol_pos, symbol
             in enumerate(symbols) if symbol == target]
    first, last = zeros[0], zeros[-1]
    distances[:first] = [first - pos for pos in range(first)]
    distances[last + 1:] = [
        pos - last for pos in range(last + 1, len(symbols))]
    for prev, next in zip(zeros, zeros[1:]):
        distances[prev + 1:next] = [
            min(pos - prev, next - pos) for pos in range(prev + 1, next)]
    return distances


if __name__ == '__main__':
    input()
    print(*distances_to_symbol(input().split(' ')))
