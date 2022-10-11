""" Imitation of two square cubes and make statistic of 1000 iterations"""

import collections
import random
from prettytable import PrettyTable


def dice():
    """imitation of two square cubes"""
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a + b


def make_statistic(throws=1000):
    """throw dice and remember in statistic"""
    statistic_throw = collections.Counter()
    throw = 0
    while throw < throws:
        statistic_throw[dice()] += 1
        throw += 1
    statistic_throw_sorted = sorted(statistic_throw.items())
    return statistic_throw_sorted, throws


def make_table(data: list, throws: int):
    """print table with data"""
    table = PrettyTable()
    table.field_names = ['number', 'percent simulations']
    # print(len(data))
    for i in data:
        table.add_row([i[0], round(float(i[1] / throws * 100), 3)])
    table.add_column('expected data', [2.78, 5.56, 8.3, 11.11, 13.89, 16.67, 13.89, 11.11, 8.3, 5.56, 2.78])
    return table


def main():
    """main controller"""
    stats, throws = make_statistic(number_of_throws)
    return make_table(stats, throws)


if __name__ == '__main__':
    number_of_throws = 1000
    print(main())
