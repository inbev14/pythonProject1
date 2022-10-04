from prettytable import PrettyTable
import re


def check_file(filename: str):
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(f"{error},\nFile has not found!")
    except UnicodeDecodeError as error:
        return str(f"{error},\nFile is wrong type!")


def read_file(filename: str):
    """Read txt file """
    with open(filename) as file:
        return [re.findall(r'\w+', data) for data in file.readlines()]


def find_element(data: list, el_number: str):
    """return element by atomic number"""
    for number in data:
        if number[0] == el_number:
            return number


def main():
    el_number = input("Enter element atomic number : ")
    element = find_element()
    chem_table = PrettyTable()
    chem_table.field_names = ['Atomic Number', 'Symbol', 'Chemical Element']
    chem_table.add_row(element)
    print(chem_table)
    return chem_table


if __name__ == '__main__':
    filename = 'elements.txt'
    check_file(filename)
    main()
