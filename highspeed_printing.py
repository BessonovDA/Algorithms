# Задача: B. Ловкость рук
# Успешная попытка 80132870 от 28 дек 2022, 19:34:41

def highspeed_printing(numbers, buttons,
                       collection_of_buttons='123456789', players=2):
    return sum(
        (buttons * players >= numbers.count(button) > 0)
        for button in collection_of_buttons)


if __name__ == '__main__':

    print(highspeed_printing(
        buttons=int(input()),
        numbers=f'{input()}{input()}{input()}{input()}'))
