def find_numbers(start=0, stop=0):
    """Find numbers in range(start,stop) that are equal to the sum of powers of their numbers"""
    if not str(start).isdigit() or not str(stop).isdigit():
        return "Wrong input data! Enter numbers only!"
    numbers = [number for number in range(start, stop)]
    wanted_numbers = []
    for number in numbers:
        number_powers = [number_index for number_index in range(1, len(str(number)) + 1)]
        sum_digits_number = sum(list(map(lambda x, y: pow(int(x), y), str(number), number_powers)))
        if number == sum_digits_number:
            wanted_numbers.append(number)
    return wanted_numbers


if __name__ == '__main__':
    CASES = {
        (1, 10): [1, 2, 3, 4, 5, 6, 7, 8, 9],
        (1, 100): [1, 2, 3, 4, 5, 6, 7, 8, 9, 89],
        (1, 1000): [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598],
        (1, 10000): [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598, 1306, 1676, 2427],
        (): [],
    }
    for case, answer in CASES.items():
        assert find_numbers(*case) == answer
        
        
        # assert find_numbers() == []
       
        # assert find_numbers(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
        # assert find_numbers(1, 1000) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598]
        # assert find_numbers(1, 10000) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598, 1306, 1676, 2427]
        # assert find_numbers() == []
