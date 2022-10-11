""" Imitation of two square cubes and make statistic of 1000 iterations"""
# import namedtuple
import collections
import random
from prettytable import PrettyTable


def dice() -> int:
    """imitation of two square cubes"""
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a + b


def make_statistic(throws: int) -> tuple[list[tuple[int, int]], int]:
    """throw dice and remember in statistic"""
    statistic_throw = collections.Counter()
    for _ in range(throws):
        statistic_throw[dice()] += 1
    statistic_throw_sorted = sorted(statistic_throw.items())
    return statistic_throw_sorted, throws


def make_table(data: list, throws: int) -> PrettyTable:
    """return table with data"""
    table = PrettyTable()
    table.field_names = ['number', 'percent simulations']
    for i in data:
        table.add_row([i[0], round(float(i[1] / throws * 100), 3)])
    table.add_column('expected data', [2.78, 5.56, 8.3, 11.11, 13.89, 16.67, 13.89, 11.11, 8.3, 5.56, 2.78])
    return table


def main() -> PrettyTable:
    """main controller"""
    stats, throws = make_statistic(number_of_throws)
    return make_table(stats, throws)


if __name__ == '__main__':
    number_of_throws = int(input("Enter qty throws: "))
    print(main())
