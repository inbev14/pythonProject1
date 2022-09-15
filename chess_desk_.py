def start_prog():
    """Перевірка першої координати й другої в залежності від її парності"""
    if check_request():
        if check_coord_1():
            return check_coord_even()
        else:
            return check_coord_odd()


def check_request():
    """ Перевірка запроса на хибу"""
    if len(coordinate) == 2:                        # перевірка довжини
        if not coordinate[0].isdigit():             # Перевірка першого символу на букву
            if coordinate[0].lower() in lines:        # перевірка першого на збіг потрібних букв
                if coordinate[1].isdigit():         # перевірка другого символу на цифру
                    if 0 < int(coordinate[1]) < 9:      # перевірка цифри на величину
                        return True
    print("Enter correct request")
    return False


def find_letter():
    """ Проходить за списком і повертає літеру """
    for letter in lines:
        if coordinate[0].lower() == letter:
            return letter
    else:
        print("Enter correct coordinate")
        return False


def check_coord_1():
    """Перевірка першої координати (букви), якщо парна, то Тру і навпаки"""
    letter = find_letter()
    if letter:
        if lines.index(letter) % 2 == 0:
            return True
        else:
            return False
    return False


def check_coord_even():
    """Перевірка другого символу (числа) координата на парність, якщо буква парна"""
    if int(coordinate[1]) % 2 == 0:
        return "white"
    else:
        return "black"


def check_coord_odd():
    """Перевірка другого символу (числа) координата на парність, якщо буква не парна"""
    if int(coordinate[1]) % 2 == 0:
        return "black"
    else:
        return "white"


# запуск програми у циклі з можливістю виходу
# програму написав без функції через глобальні змінні "coordinate" i "lines"
while True:
    start = input("\nEnter any key to continue, 'q' to quit:\n")
    if start == "q":
        break
    lines = ["a", "b", "c", "d", "e", "f", "g", "h"]
    coordinate = input("Please, enter coordinate to find out what color it is, like 'a1'. \n"
                       "(You must enter one letter from 'a' to 'h' and one number from 1 to 8 only): \n")
    prog = start_prog()
    if prog:
        print(f"Your coordinate '{coordinate}' is {prog}.")
