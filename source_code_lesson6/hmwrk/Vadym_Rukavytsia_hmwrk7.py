from prettytable import PrettyTable
import re


def check_file(filename: str):
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(f"{error},\nFile has not found!")
    except UnicodeDecodeError as error:
        return str(f"{error},\nFile is wrong type!")


def check_request(element):
    if isinstance(element, int):
        return int(element)
    elif isinstance(element, str):
        return str(element)


def read_file(filename: str):
    """Read txt file and return list with data"""
    with open(filename) as file:
        return [re.findall(r'\w+', data) for data in file.readlines()]


def find_element(data: list, element):
    """return element by atomic number"""
    for elem in data:
        if element.isdigit():
            if elem[0] == element:
                return elem
            return False
        elif element.isinsta
    return False


def main():
    """main controller"""
    element = input("Enter element or his number (Enter to quit): ")
    if element == "":
        print("Ok, Good Bye")
        exit()
    data = read_file(filename)
    element = find_element(data, element)
        if element:
            chem_table = PrettyTable()
            chem_table.field_names = ['Atomic Number', 'Symbol', 'Chemical Element']
            chem_table.add_row(element)
            print(chem_table)
        return chem_table
        


if __name__ == '__main__':
    filename = '../add_files/elements.txt'
    if check_file(filename):
        while True:
            main()
        
