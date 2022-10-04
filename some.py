import json
import re


def read_file():
    """Read txt file """
    filename = 'elements.txt'
    with open(filename) as file:
        return [re.findall(r'\w+', data) for data in file.readlines()]


def main():
    """return element by atomic number"""
    el_number = input("Enter number of element")
    # key for key in data.keys():
    #     print()
    for number, element_info in data.items():
        if number == el_number:
            print(data[number])
            
            
if __name__ == '__main__':
    main()
    
    
    