from string import ascii_lowercase


def start_prog():
    """Перевірка першої координати й другої в залежності від її парності"""
    first_coord = check_coord_1()
    if first_coord == "even":
        color = check_coord_2()
    elif first_coord == "odd":
        color = not check_coord_2()
    else:
        return False
    return "white" if color else "black"
    
    
def check_request():
    """ Перевірка запроса на хибу або на вихід із програми"""
    if coordinate == 'q':
        print("Thank you, good bye!")
        exit()
    if len(coordinate) == 2:                          # перевірка довжини
        if coordinate[0].isalpha():                   # Перевірка першого символу на букву
            if coordinate[0].lower() in lines:        # перевірка першого на збіг потрібних букв і запам'ятати букву
                letter = coordinate[0].lower()
                if coordinate[1].isdigit():           # перевірка другого символу на цифру
                    if 0 < int(coordinate[1]) < size+1:    # перевірка цифри на величину
                        return letter
    print("-" * 25 + "\nEnter correct request!\n" + "-" * 25)


def check_coord_1():
    """Перевірка першої координати (букви), якщо парна, то Тру і навпаки"""
    letter = check_request()
    if letter:
        return "even" if lines.index(letter) % 2 == 0 else "odd"
    return False


def check_coord_2():
    """Перевірка другого символу (числа) координата на парність, якщо буква парна"""
    if int(coordinate[1]) % 2 == 0:
        return True
    else:
        return False


# запуск програми у циклі з можливістю виходу
# саму програму написав без функції через глобальні змінні "coordinate" i "lines"
while True:
    size = 8
    lines = ascii_lowercase[:size]
    coordinate = input("Do you want to find out what color is cell on chessboard?\n"
                       "Enter coordinate, like 'A1'  . \n"
                       "(You must enter one letter from 'A' to 'H' and one number from 1 to 8 only, "
                       "'q' to exit: \n")
    prog = start_prog()
    if prog:
        print("*" * 30 + "\n" + f"Your coordinate '{coordinate.upper()}' is {prog}" + "\n" + "*" * 30 + "\n")
